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

from logging import ERROR, INFO

from ros2caret.verb.create_architecture import CreateArchitecture


class TestCreateArchitecture:

    def test_check_created_exist_case(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=True)
        CreateArchitecture._check_created('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == INFO

    def test_check_created_not_exist_case(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=False)
        CreateArchitecture._check_created('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == ERROR
