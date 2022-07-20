from logging import ERROR, INFO
from ros2caret.verb.create_architecture import CreateArchitecture


class TestCreateArchitecture:

    def test_check_created_01(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=True)
        CreateArchitecture._check_created('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == INFO
    
    def test_check_created_02(self, caplog, mocker):
        mocker.patch('os.path.exists', return_value=False)
        CreateArchitecture._check_created('')
        assert len(caplog.records) == 1
        record = caplog.records[0]
        assert record.levelno == ERROR
