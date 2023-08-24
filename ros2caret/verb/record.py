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

import os

from typing import Optional

from caret_msgs.msg import End, Start, Status

import rclpy
from rclpy import qos
from rclpy.node import Node

from ros2caret.verb import VerbExtension
from ros2caret.verb.caret_record_init import init

from tqdm import tqdm

from tracetools_trace.tools import lttng, names, path
from tracetools_trace.tools.signals import execute_and_handle_sigint


class CaretSessionNode(Node):

    def __init__(self):
        super().__init__('caret_session_node')
        pub_qos = qos.QoSProfile(
            history=qos.HistoryPolicy.KEEP_LAST,
            depth=1,
            reliability=qos.ReliabilityPolicy.RELIABLE,
            durability=qos.DurabilityPolicy.VOLATILE
        )
        self._start_pub_ = self.create_publisher(
            Start, '/caret/start_record', pub_qos)
        self._end_pub_ = self.create_publisher(
            End, '/caret/end_record', pub_qos)

        sub_qos = qos.QoSProfile(
            history=qos.HistoryPolicy.KEEP_ALL,
            reliability=qos.ReliabilityPolicy.RELIABLE,
            durability=qos.DurabilityPolicy.VOLATILE
        )
        self._sub = self.create_subscription(
            Status, '/caret/status', self.subscription_callback, sub_qos)
        self._caret_node_names = set()
        self._progress = None
        self.started = False

    def subscription_callback(self, msg):
        if msg.status != Status.RECORD:
            return

        if msg.caret_node_name in self._caret_node_names:
            self._caret_node_names.remove(msg.caret_node_name)

        if self._progress:
            self._progress.update()

        if len(self._caret_node_names) == 0:
            self.stop_progress()
            print('All process started recording.')
            self.started = True

    def stop_progress(self):
        if self._progress:
            self._progress.close()

    def start(
        self,
        verbose: bool,
        recording_frequency: Optional[str] = None
    ) -> int:
        all_node_names = self.get_node_names()
        # NOTE: caret_trace creates nodes with the name caret_trace_[pid].
        self._caret_node_names = {
            node_name
            for node_name
            in all_node_names
            if 'caret_trace_' in node_name
        }
        caret_node_num = len(self._caret_node_names)
        if caret_node_num > 0:
            print(f'{caret_node_num} recordable processes found.')
        if verbose:
            self._progress = tqdm(
                total=caret_node_num,
                bar_format='{n}/{total} process started recording', leave=True)

        msg = Start()
        msg.recording_frequency = 100 if recording_frequency is None else int(recording_frequency)
        self._start_pub_.publish(msg)
        return caret_node_num

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
            '$ROS_TRACE_DIR if ROS_TRACE_DIR is set and not empty, or $ROS_HOME/tracing,'
            ' using ~/.ros for ROS_HOME if not set or if empty)')
        parser.add_argument(
            '-l', '--list', dest='list', action='store_true',
            help='display lists of enabled events and context names '
            '(default: %(default)s)')
        parser.add_argument(
            '-v', '--verbose', dest='verbose', action='store_true',
            help='display status of recording')
        parser.add_argument(
            '-f', '--recording-frequency', dest='recording_frequency',
            help=('recording frequency for Initialization-related trace points (default: 100Hz). '
                  'Higher frequencies allow recording in a shorter time. '
                  'However, the possibility of recording failure increases. '))
        parser.add_argument(
            '--light', dest='light_mode', action='store_true',
            help='light mode (record high level events only)')
        parser.add_argument(
            '--subbuffer-size-ust', dest='subbuffer_size_ust', type=int,
            default=8*4096,
            help='the size of the subbuffers for userspace events(default: 8*4096). '
                 'buffer size must be power of two. '
                 'available in iron or rolling only. ')
        parser.add_argument(
            '--subbuffer-size-kernel', dest='subbuffer_size_kernel', type=int,
            default=32*4096,
            help='the size of the subbuffers for kernel events(default: 32*4096). '
                 'buffer size must be power of two. '
                 'available in iron or rolling only. ')

    def main(self, *, args):
        if args.light_mode:
            events_ust = [
                    'ros2:*callback*',
                    'ros2_caret:*callback*',
                    'ros2:dispatch*',
                    'ros2_caret:dispatch*',
                    'ros2:rclcpp*',
                    'ros2_caret:rclcpp*',
                    'ros2_caret:rmw*',
                    'ros2:rmw_take',
                    '*callback_group*',
                    'ros2_caret:*executor',
                    'ros2_caret:dds_bind*',
                    'ros2:rcl_*init',
                    'ros2_caret:rcl_*init',
                    'ros2_caret:caret_init']
            if os.environ['ROS_DISTRO'] in ['iron' or 'rolling']:
                events_ust.append('ros2:rcl_publish')
        else:
            events_ust = ['ros*']
        context_names = names.DEFAULT_CONTEXT
        events_kernel = []

        rclpy.init()
        node = CaretSessionNode()

        init_args = {}
        init_args['session_name'] = args.session_name
        init_args['base_path'] = args.path
        init_args['ros_events'] = events_ust
        init_args['kernel_events'] = events_kernel
        # Note: key name of context_fields differs in galactic and humble,
        if os.environ['ROS_DISTRO'] == 'galactic':
            init_args['context_names'] = context_names
        else:
            init_args['context_fields'] = context_names
        init_args['display_list'] = args.list
        # Note: keyword argument --subbuffer_size_ust/kernel are available in iron or rolling.

        if os.environ['ROS_DISTRO'] not in ['iron', 'rolling'] \
                and args.subbuffer_size_ust != 8*4096:
            raise ValueError('the --subbuffer-size-ust option is '
                             'available in iron or rolling')
        if args.subbuffer_size_ust & (args.subbuffer_size_ust-1):
            raise ValueError('--subbuffer-size-ust value must be power of two.')
        init_args['subbuffer_size_ust'] = args.subbuffer_size_ust

        if os.environ['ROS_DISTRO'] not in ['iron', 'rolling'] \
                and args.subbuffer_size_kernel != 32*4096:
            raise ValueError('the --subbuffer-size-kernel option is '
                             'available in iron or rolling')
        if args.subbuffer_size_kernel & (args.subbuffer_size_kernel-1):
            raise ValueError('--subbuffer-size-kernel value must be power of two.')
        init_args['subbuffer_size_kernel'] = args.subbuffer_size_kernel
        init(**init_args)

        def _run():
            recordable_node_num = node.start(args.verbose, args.recording_frequency)
            while not node.started and recordable_node_num > 0:
                rclpy.spin_once(node)
            input('press enter to stop...')

        def _fini():
            node.stop_progress()
            node.end()
            print('stopping & destroying tracing session')
            lttng.lttng_fini(session_name=args.session_name)

        execute_and_handle_sigint(_run, _fini)

        return 0
