import os

import ran.config


def test_get_config_dir():
    assert ran.config.get_config_dir() == (
        os.path.expanduser("~") + '/.config/ran')


def test_get_data_file():
    assert ran.config.get_data_file() == (
        os.path.expanduser("~") + '/.config/ran/data.json')
