import os

from ran.config import get_config_dir, get_data_file


def test_get_config_dir():
    assert get_config_dir() == os.path.expanduser("~") + '/.config/ran'


def test_get_data_file():
    assert get_data_file() == (
        os.path.expanduser("~") + '/.config/ran/data.json')
