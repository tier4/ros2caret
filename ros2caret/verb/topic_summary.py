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

from .summary import Summary


class TopicSummaryVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            'trace_dir', type=str,
            help='the path to the trace directory'
        )
        parser.add_argument(
            '--duration_filter', dest='d_filter_args',
            type=float, nargs='+',
            help=('Load only this duration from the offset. '
                  'arg 1: duration [s], arg 2: offset [s]. '),
            required=False
        )
        parser.add_argument(
            '--strip_filter', dest='s_filter_args',
            type=float, nargs='+',
            help=('Ignore trace data for specified seconds from start/end. '
                  'arg 1: left split [s], arg 2: right split [s]. '),
            required=False
        )
        parser.add_argument(
            '-c', '--display_check', dest='display_check', action='store_true',
            help='display the error checks to the trace results.',
            required=False
        )

    def main(self, *, args):
        summary = Summary(args, 'topic_name')
        summary.print_summary()
