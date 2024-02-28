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


from logging import getLogger

from caret_analyze import Architecture, Lttng
from caret_analyze.architecture import MAX_CALLBACK_CONSTRUCTION_ORDER_ON_PATH_SEARCHING
from ros2caret.verb import VerbExtension

logger = getLogger(__name__)


class CheckCTFVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            'trace_dir', type=str,
            help='the path to the trace directory to be checked')
        parser.add_argument(
            '-m', '--max_callback_construction_order_on_path_searching',
            type=int, dest='max_callback_construction_order_on_path_searching',
            help='callbacks whose construction_order are greater than'
            ' this value are ignored on path searching.'
            ' The value must be positive integer or "0". "0" means unlimited.'
            ' Default: %(default)s',
            required=False, default=MAX_CALLBACK_CONSTRUCTION_ORDER_ON_PATH_SEARCHING,
        )

    def main(self, *, args):
        try:
            if args.max_callback_construction_order_on_path_searching >= 0:
                Lttng(args.trace_dir)
                Architecture(
                    'lttng',
                    args.trace_dir,
                    args.max_callback_construction_order_on_path_searching
                )
            else:
                raise ValueError(
                    'error: argument',
                    '-m/--max_callback_construction_order_on_path_searching',
                    '(%s)' % args.max_callback_construction_order_on_path_searching
                )
        except Exception as e:
            logger.warning(e)
