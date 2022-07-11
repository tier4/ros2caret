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

from logging import ERROR, INFO, WARNING

from ros2caret.verb.check_caret_rclcpp import RclcppCheck


class TestCheckCaretRclcpp:

    def test_file_exist(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=True)
        mocker.patch(
            'ros2caret.verb.check_caret_rclcpp.RclcppCheck._get_obj_paths', return_value=[])
        RclcppCheck('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == INFO

    def test_ng_case(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=True)
        base_path = 'ros2caret.verb.check_caret_rclcpp.RclcppCheck.'
        mocker.patch(base_path+'_get_obj_paths', return_value=[''])
        mocker.patch(base_path+'_has_caret_rclcpp_tp', return_value=False)

        RclcppCheck('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == WARNING

    def test_ok_case(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=True)
        base_path = 'ros2caret.verb.check_caret_rclcpp.RclcppCheck.'
        mocker.patch(base_path+'_get_obj_paths', return_value=[''])
        mocker.patch(base_path+'_has_caret_rclcpp_tp', return_value=True)

        RclcppCheck('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == INFO

    def test_file_not_exist(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=False)
        try:
            RclcppCheck('')
        except SystemExit as e:
            assert e.args == (1,)
            assert len(caplog.records) == 1
            record = caplog.records[0]
            assert record.levelno == ERROR

    def test_get_package_name(self):
        get_package_name = RclcppCheck._create_get_package_name('')
        assert get_package_name('foo/bar/baz') == 'foo'

        get_package_name = RclcppCheck._create_get_package_name('foo/')
        assert get_package_name('foo/bar/baz') == 'bar'

        get_package_name = RclcppCheck._create_get_package_name('foo/bar/')
        assert get_package_name('foo/bar/baz') == 'baz'
