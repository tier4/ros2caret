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


class RecordSimTime(VerbExtension):

    def add_arguments(self, parser, cli_name):
        pass

    def main(self, *, args):
        raise NotImplementedError('disabled')
        # lttng = Lttng(args.trace_dir, force_conversion=True)
        # app = Application(args.architecture_path, 'yaml', lttng)
        # path = app.path[args.path_name]

        # message_flow(path, export_path=args.output_path,
        #              granularity=args.granularity)
