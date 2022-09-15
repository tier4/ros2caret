# Copyright 2021 Research Institute of Systems Planning, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from ros2caret.verb import VerbExtension

import rclpy
from tqdm import tqdm

from rclpy.node import Node
from tracetools_trace.tools import names, path
from tracetools_trace.trace import fini
from tracetools_trace.trace import init

from caret_msgs.msg import Start, Status, End


class CaretSessionNode(Node):

    def __init__(self):
        super().__init__('caret_session_node')
        self._start_pub_ = self.create_publisher(Start, '/caret/start_record', 10)
        self._end_pub_ = self.create_publisher(End, '/caret/end_record', 10)
        self._sub = self.create_subscription(
            Status, '/caret/status', self.subscription_callback, 100)
        self._node_names = set()
        self._progress = None
        self.started = False

    def subscription_callback(self, msg):
        self._node_names.remove(msg.node_name)

        if self._progress:
            self._progress.update()

        if len(self._node_names) == 0:
            if self._progress:
                self._progress.close()
            print('All process started recording.')
            self.started = True

    def start(self, verbose: bool):
        all_node_names = self.get_node_names()

        # NOTE: caret_trace creates nodes with the name caret_trace_[pid].
        self._node_names = {
            node_name
            for node_name
            in all_node_names
            if 'caret_trace_' in node_name
        }

        caret_node_num = len(self._node_names)
        print(f'{caret_node_num} recordable processes found.')
        if verbose:
            self._progress = tqdm(
                total=caret_node_num,
                bar_format='{n}/{total} process started recording',
                leave=True)

        msg = Start()
        self._start_pub_.publish(msg)

    def end(self):
        msg = End()
        self._end_pub_.publish(msg)


class RecordVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            '-s', '--session-name', dest='session_name',
            default=path.append_timestamp('session'),
            help='the name of the tracing session (default: session-YYYYMMDDHHMMSS)')
        parser.add_argument(
            '-p', '--path', dest='path',
            help='path of the base directory for trace data (default: '
            '$ROS_TRACE_DIR if ROS_TRACE_DIR is set and not empty, or '
            '$ROS_HOME/tracing, using ~/.ros for ROS_HOME if not set or if empty)')
        parser.add_argument(
            '-l', '--list', dest='list', action='store_true',
            help='display lists of enabled events and context names (default: %(default)s)')
        parser.add_argument(
            '-v', '--verbose', dest='verbose', action='store_true',
            help='dieplay status of recording')

    def main(self, *, args):
        events_ust = ['ros*']
        context_names = names.DEFAULT_CONTEXT
        events_kernel = []

        rclpy.init()
        node = CaretSessionNode()

        init(
            session_name=args.session_name,
            base_path=args.path,
            ros_events=events_ust,
            kernel_events=events_kernel,
            context_names=context_names,
            display_list=args.list,
        )

        node.start(args.verbose)
        while not node.started:
            rclpy.spin_once(node)

        fini(
            session_name=args.session_name,
        )

        node.end()

        return 0
