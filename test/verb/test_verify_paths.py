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

from logging import INFO

from ros2caret.verb.verify_paths import VerifyPaths


class TestVerifyPaths:

    def test_verify_ok_case(self, caplog, mocker):
        path_mock = mocker.Mock()
        mocker.patch.object(path_mock, 'verify', return_value=True)
        architecture_mock = mocker.Mock()
        mocker.patch.object(architecture_mock,
                            'get_path',
                            return_value=path_mock)

        verify_paths = VerifyPaths('', architecture_mock)
        verify_paths.verify(['verified_path_name'])
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == INFO

    def test_verify_ng_case(self, caplog, mocker):
        path_mock = mocker.Mock()
        mocker.patch.object(path_mock, 'verify', return_value=False)
        architecture_mock = mocker.Mock()
        mocker.patch.object(architecture_mock,
                            'get_path',
                            return_value=path_mock)

        verify_paths = VerifyPaths('', architecture_mock)
        verify_paths.verify(['verified_path_name'])
        assert len(caplog.records) == 0
