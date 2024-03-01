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
import os
from typing import List, Optional

try:
    import caret_analyze
    from caret_analyze import DEFAULT_MAX_CALLBACK_CONSTRUCTION_ORDER_ON_PATH_SEARCHING
    Architecture = caret_analyze.Architecture
except ModuleNotFoundError as e:
    if 'GITHUB_ACTION' in os.environ:
        Architecture = None
    else:
        raise(e)

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
        parser.add_argument(
            '-m', '--max_callback_construction_order_on_path_searching',
            type=int, dest='max_callback_construction_order_on_path_searching',
            help='callbacks whose construction_order are greater than'
            ' this value are ignored on path searching.'
            ' The value must be positive integer or "0". "0" means unlimited.'
            ' Default: %(default)s',
            required=False, default=DEFAULT_MAX_CALLBACK_CONSTRUCTION_ORDER_ON_PATH_SEARCHING,
        )

    def main(self, *, args):
        try:
            verify_paths = VerifyPaths(args.arch_path,
                                       args.max_callback_construction_order_on_path_searching)
            verify_paths.verify(args.verified_path_names)
        except Exception as e:
            logger.info(e)


class VerifyPaths:

    def __init__(
        self,
        arch_path: str,
        max_callback_construction_order_on_path_searching: int,
        architecture: Optional[Architecture] = None
    ) -> None:
        if architecture:
            self._arch = architecture
        else:
            if max_callback_construction_order_on_path_searching >= 0:
                self._arch = Architecture(
                    'yaml',
                    arch_path,
                    max_callback_construction_order_on_path_searching
                )
            else:
                raise ValueError(
                    'error: argument',
                    '-m/--max_callback_construction_order_on_path_searching',
                    '(%s)' % max_callback_construction_order_on_path_searching
                )

    def verify(
        self,
        verified_path_names: Optional[List[str]]
    ) -> None:
        verified_path_names = (verified_path_names
                               or self._arch.path_names)

        for path_name in verified_path_names:
            print(f'\n=============== [{path_name}] ===============')
            path = self._arch.get_path(path_name)
            if path.verify():
                logger.info(
                    'No problem. '
                    f'CARET can calculate the latency of `{path_name}`'
                )
