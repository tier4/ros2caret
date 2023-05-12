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

import os

from ros2caret.verb import VerbExtension


class CaretVersionVerb(VerbExtension):

    def main(self, *, args):
        current_dir = os.path.dirname(os.path.realpath(__file__))
        parent_dir = os.path.abspath(os.path.join(current_dir, '../..'))
        setup_path = os.path.join(parent_dir, 'setup.py')
        with open(setup_path, 'r') as file:
            for line in file:
                if 'version=' in line:
                    version = line.replace("version='", '')
                    version = version.replace("'", '')
                    version = version.replace(',', '').strip()
                    print(version)
                    break
