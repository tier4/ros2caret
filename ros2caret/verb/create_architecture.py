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
from typing import Optional

try:
    import caret_analyze
    Architecture = caret_analyze.Architecture
    Error = caret_analyze.exceptions.Error
    CatchErrors = (OSError, Error)
except ModuleNotFoundError as e:
    if 'GITHUB_ACTION' in os.environ:
        Architecture = None
        CatchErrors = OSError
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

root_logger = getLogger()
root_logger.removeHandler(root_logger.handlers[0])

logger = getLogger(__name__)
logger.setLevel(INFO)
logger.addHandler(handler)


class CreateArchitectureVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument(
            'trace_dir', type=str,
            help='the path to the main trace directory'
        )
        parser.add_argument(
            '-o', '--output_path', dest='output_path', type=str,
            help='the path to the output architecture file',
            required=False, default='./architecture.yaml'
        )
        parser.add_argument(
            '-f', '--force', dest='force', action='store_true',
            help='allow overwrite of architecture file',
            required=False, default=False
        )

    def main(self, *, args):
        create_arch = CreateArchitecture(args.trace_dir)
        create_arch.create(args.output_path, args.force)


class CreateArchitecture:

    def __init__(
        self,
        trace_dir: str,
        architecture: Optional[Architecture] = None
    ) -> None:
        if architecture:
            self._arch = architecture
        else:
            self._arch = Architecture('lttng', trace_dir)

    def create(self, output_path: str, force: bool) -> None:
        try:
            self._arch.export(output_path, force)
        except CatchErrors as e:
            logger.error(f'{e} Failed to create architecture file.')
        else:
            logger.info('Architecture file successfully created. '
                        f'PATH: {os.path.abspath(output_path)}')
