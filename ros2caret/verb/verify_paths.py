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

from logging import Formatter, getLogger, INFO, StreamHandler

from caret_analyze import Architecture

from ros2caret.verb import VerbExtension


handler = StreamHandler()
handler.setLevel(INFO)

fmt = '%(levelname)-8s: %(asctime)s | %(message)s'
formatter = Formatter(
    fmt,
    datefmt='%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)

logger = getLogger(__name__)
logger.setLevel(INFO)
logger.addHandler(handler)


class VerifyPathsVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            'arch_path', type=str,
            help='the path to the architecture file'
        )
        parser.add_argument(
            '-p', '--verified_path_names', dest='verified_path_names',
            type=str, nargs='+',
            help='path names to be verified.',
            required=False,
        )

    def main(self, *, args):
        arch = Architecture('yaml', args.arch_path)
        verified_path_names = args.verified_path_names or arch.path_names

        for path_name in verified_path_names:
            print(f'\n=============== [{path_name}] ===============')
            path = arch.get_path(path_name)
            if path.verify():
                logger.info('No problem.')
