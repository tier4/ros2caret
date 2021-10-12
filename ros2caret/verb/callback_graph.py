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

from caret_analyze import Application
from caret_analyze.plot import callback_graph
from ros2caret.verb import VerbExtension


class CallbackGraphVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            '-a', '--architecture_path', type=str, dest='architecture_path',
            help='the path to the architecture file', required=True)

        parser.add_argument(
            '-o', '--output_path', dest='output_path', type=str,
            help='the output path to the callback graph file', required=True)

        parser.add_argument(
            '-p', '--path_name', dest='path_name', type=str, default=None,
            help='the path_name to highlight')

        parser.add_argument(
            '-s', '--separate', dest='separate', type=bool, default=False,
            help='If True, split topics. default: false.')

        parser.add_argument(
            '-t', '--target_path_only', dest='target_path_only', type=bool, default=False,
            help='Show only the path of the target. The path must be specified with --path_name.')

    def main(self, *, args):
        app = Application(args.architecture_path, 'yaml', None)
        callbacks = []
        if args.path_name:
            path = app.path[args.path_name]
            callbacks = path.callbacks
        callback_graph(
            app._arch, callbacks, args.output_path, args.separate, args.target_path_only
        )
