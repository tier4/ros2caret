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
import requests
from bs4 import BeautifulSoup

class CaretVersionVerb(VerbExtension):
    
    def _get_latest_caret_version(self):

        CARET_LATEST_VERSION_URL = 'https://github.com/tier4/caret/tags'

        response = requests.get(CARET_LATEST_VERSION_URL)
        soup = BeautifulSoup(response.content, 'html.parser')

        version_tag = soup.find('h2', {'class': 'f4 d-inline'})
        version_tag = version_tag.find('a')
        # print(version_tag)
        
        return version_tag


    def main(self, *, args):
        latest_version = self._get_latest_caret_version()
        print(latest_version.text)
    
        
