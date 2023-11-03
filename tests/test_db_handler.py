import pytest


class TestDbHandler:
    @pytest.fixture
    def mock_config(self, monkeypatch):
        def mocked_config(key):
            config = {
                'DB_URL': 'mocked_db_url',
                'DB_USERNAME': 'mocked_db_username',
                'DB_PASSWORD': 'mocked_db_password',
                'OK_MSG': 'mocked_ok_msg',
                'NOK_MSG': 'mocked_nok_msg'
            }
            return config.get(key)

        monkeypatch.setattr('decouple.config', mocked_config)
        #mocker.patch('decouple.config', side_effect=mocked_config)

    @pytest.fixture
    def db_handler(self):
        from src.db_handler import DbHandler
        db_handler = DbHandler()
        return db_handler

    def test_connect_to_database(self, mock_config, db_handler):
        connection_msg = db_handler.connect_to_database()
        expected_msg = "I am connecting to mocked_db_url as mocked_db_username with pass: mocked_db_password..."
        assert connection_msg == expected_msg

    def test_show_msg_when_connected(self, mock_config, db_handler):
        ok_msg = db_handler.show_msg_when_connected()
        assert ok_msg == 'mocked_ok_msg'

    def test_show_msg_when_interrupted(self, mock_config, db_handler):
        nok_msg = db_handler.show_msg_when_interrputed()
        assert nok_msg == 'mocked_nok_msg'
