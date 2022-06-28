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
        assert get_package_name('foo/bar/hoge') == 'foo'

        get_package_name = RclcppCheck._create_get_package_name('foo/')
        assert get_package_name('foo/bar/hoge') == 'bar'

        get_package_name = RclcppCheck._create_get_package_name('foo/bar/')
        assert get_package_name('foo/bar/hoge') == 'hoge'
