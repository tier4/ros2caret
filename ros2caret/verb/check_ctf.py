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
# limitations under the License.from caret_analyze import Application, Lttng


from logging import getLogger

from caret_analyze import Architecture, Lttng
from caret_analyze.exceptions import Error
from ros2caret.verb import VerbExtension

logger = getLogger(__name__)


class CheckCTFVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            '-d', '--trace_dir', dest='trace_dir', type=str,
            help='the path to the trace directory to be checked', required=True)

    def main(self, *, args):
        try:
            Lttng(args.trace_dir)
            Architecture('lttng', args.trace_dir)
        except Error as e:
            logger.warning(e)
