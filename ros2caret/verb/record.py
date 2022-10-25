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

from ros2caret.verb import VerbExtension

from tracetools_trace.tools import names, path
from tracetools_trace.trace import fini
from tracetools_trace.trace import init


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

    def main(self, *, args):
        events_ust = ['ros*']
        context_fields = names.DEFAULT_CONTEXT
        events_kernel = []

        init_args = {}
        init_args['session_name'] = args.session_name
        init_args['base_path'] = args.path
        init_args['ros_events'] = events_ust
        init_args['kernel_events'] = events_kernel
        # Note: key name of context_fields differs in galactic and humble,
        if os.environ['ROS_DISTRO'] == 'galactic':
            init_args['context_names'] = context_fields
        else:
            init_args['context_fields'] = context_fields
        init_args['display_list'] = args.list

        init(**init_args)
        fini(session_name=args.session_name)

        return 0
