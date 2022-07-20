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

    def main(self, *, args):
        CreateArchitecture(args.trace_dir, args.output_path)


class CreateArchitecture:

    def __init__(self, trace_dir: str, output_path: str) -> None:
        arch = Architecture('lttng', trace_dir)
        arch.export(output_path)

        CreateArchitecture._check_created(output_path)

    @staticmethod
    def _check_created(output_path: str) -> None:
        if os.path.exists(output_path):
            logger.info('Architecture file successfully created. '
                        f'PATH: {os.path.abspath(output_path)}')
        else:
            logger.error('Failed to create architecture file.')
