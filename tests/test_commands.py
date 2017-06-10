import os
import pytest
import json

import ran.commands
import ran.config
import tests.test_screen


def test_hlp(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 18)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    ran.commands.hlp()

    out, err = capsys.readouterr()
    text = (
        '\n\t \x1b[4;93mHelp\x1b[0m\n\n' +
        '\t Commands:\n' +
        '\t\t \x1b[93mh, help\x1b[0m - display this help text\n' +
        '\t\t \x1b[93ml, log\x1b[0m  - log workout\n' +
        '\t\t \x1b[93mq, quit\x1b[0m - exit ran\n\n\n\n')

    assert out == text


def test_stats(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 10)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    ran.commands.stats('')

    out, err = capsys.readouterr()

    assert out == '\n\n'


class TestCommands:

    @pytest.fixture(
        scope='class',
        params=['h', 'help'])
    def helps(self, request):
        return request.param

    def test_commands_with_help_arg(self, monkeypatch, capsys, helps):
        def mockreturn():
            print(42)

        monkeypatch.setattr(ran.commands, 'hlp', mockreturn)
        ran.commands.commands(helps)

        out, err = capsys.readouterr()

        assert out == '42\n'

    @pytest.fixture(
        scope='class',
        params=['l', 'log'])
    def logs(self, request):
        return request.param

    def test_commands_with_log_arg(self, monkeypatch, capsys, logs):
        def mockreturn():
            print('log')

        monkeypatch.setattr(ran.commands, 'log', mockreturn)
        ran.commands.commands(logs)

        out, err = capsys.readouterr()

        assert out == 'log\n'

    def test_commands_with_default_arg(self, monkeypatch, capsys):
        def mockreturn(cmd):
            print(cmd)

        monkeypatch.setattr(ran.commands, 'stats', mockreturn)
        ran.commands.commands('42')

        out, err = capsys.readouterr()

        assert out == '42\n'


class TestLog:

    @pytest.fixture()
    def fake_get_data(self, request):
        with open('./fake.json', 'w') as f:
            json.dump(
                {'workouts': []},
                f,
                indent=4,
                ensure_ascii=False,
                separators=(', ', ': '))

        def fin():
            os.remove('./fake.json')
        request.addfinalizer(fin)

    def test_log_when_get_date_throw_cancel(self, fake_get_data, monkeypatch):
        def mock(c, w, f):
            return (c, tests.test_screen.workout())

        def mocke(c, w):
            return (True, tests.test_screen.workout())

        monkeypatch.setattr(ran.config, 'get_data_file', lambda: './fake.json')
        monkeypatch.setattr(ran.screen, 'get_date', mocke)
        monkeypatch.setattr(ran.screen, 'get_run_strength', mock)

        ran.commands.log()

        fl = ran.config.get_data_file()
        with open(fl, 'r') as f:
            data = json.load(f)

        assert data['workouts'] == []

    def test_log_when_get_run_strength_throw_cancel(
            self,
            fake_get_data,
            monkeypatch):

        def mock(c, w):
            return (True, tests.test_screen.workout())

        def mocke(c, w, f):
            return (c, tests.test_screen.workout())

        monkeypatch.setattr(ran.config, 'get_data_file', lambda: './fake.json')
        monkeypatch.setattr(ran.screen, 'get_date', mock)
        monkeypatch.setattr(ran.screen, 'get_run_strength', mocke)

        ran.commands.log()

        fl = ran.config.get_data_file()
        with open(fl, 'r') as f:
            data = json.load(f)

        assert data['workouts'] == []

    def test_log_when_get_date_change_workout(
            self,
            fake_get_data,
            monkeypatch):

        def mock(c, w):
            return (c, tests.test_screen.workout())

        def mocke(c, w, f):
            return (c, w)

        monkeypatch.setattr(ran.config, 'get_data_file', lambda: './fake.json')
        monkeypatch.setattr(ran.screen, 'get_date', mock)
        monkeypatch.setattr(ran.screen, 'get_run_strength', mocke)

        ran.commands.log()

        fl = ran.config.get_data_file()
        with open(fl, 'r') as f:
            data = json.load(f)

        assert data['workouts'] == [tests.test_screen.workout()]

    def test_log_when_get_run_strength_change_workout(
            self,
            fake_get_data,
            monkeypatch):

        def mock(c, w):
            return (c, w)

        def mocke(c, w, f):
            return (c, tests.test_screen.workout())

        monkeypatch.setattr(ran.config, 'get_data_file', lambda: './fake.json')
        monkeypatch.setattr(ran.screen, 'get_date', mock)
        monkeypatch.setattr(ran.screen, 'get_run_strength', mocke)

        ran.commands.log()

        fl = ran.config.get_data_file()
        with open(fl, 'r') as f:
            data = json.load(f)

        assert data['workouts'] == [tests.test_screen.workout()]
