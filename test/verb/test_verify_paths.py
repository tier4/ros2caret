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
