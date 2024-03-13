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
import xml.etree.ElementTree as ET

from ament_index_python.packages import get_package_share_directory, PackageNotFoundError

from ros2caret.verb import VerbExtension


class CaretVersionVerb(VerbExtension):

    def main(self, *, args):
        version = self.get_version()
        print('v' + version)

    def get_version(self):
        try:
            dir_path = get_package_share_directory('ros2caret')
            xml_path = os.path.join(dir_path, 'package.xml')
            tree = ET.parse(xml_path)
            root = tree.getroot()
            version_element = root.find('version')
            if version_element is None:
                raise RuntimeError('Error: Package version not found in package.xml')
            return version_element.text
        except(PackageNotFoundError, FileNotFoundError):
            xml_path = os.path.join(get_package_share_directory('ros2caret'), 'package.xml')
            raise RuntimeError(f'Error: Cannot find {xml_path}')
