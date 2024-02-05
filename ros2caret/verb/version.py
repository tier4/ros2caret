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

import os.path
import re

from ros2caret.verb import VerbExtension


class CaretVersionVerb(VerbExtension):

    def main(self, *, args):
        version = self.get_version()
        print('v' + version)

    def get_version(self):
        version_path = f'{os.path.dirname(os.path.realpath(__file__))}/../../setup.py'
        version_pattern = re.compile(r"\s*version\s*=\s*['\"](\d+\.\d+\.\d+)['\"]")
        with open(version_path) as f:
            for line in f:
                match = version_pattern.search(line)
                if match:
                    return match.group(1)
            else:
                raise RuntimeError('Unable to find version string.')
