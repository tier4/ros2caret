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

# from ..__version__ import __version__
import os.path
import codecs


class CaretVersionVerb(VerbExtension):

    def main(self, *, args):
        rel_path = '../../setup.py'
        version = self.get_version(rel_path)
        print('v' + version)

    def read(self,rel_path):
        here = os.path.abspath(os.path.dirname(__file__))
        with codecs.open(os.path.join(here, rel_path), 'r') as fp:
            return fp.read()

    def get_version(self,rel_path):
        for line in self.read(rel_path).splitlines():
            if line.startswith('    version='):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")
