import os
import pytest
import datetime

from ran.screen import logo_lines, message, logo, stats, get_date


class TestLogo():

    def test_logo_lines(self):
        lg = [
            ' _ __ __ _ _ __  ',
            "| '__/ _` | '_ \\ ",
            '| | | (_| | | | |',
            '|_|  \\__,_|_| |_|']

        assert logo_lines() == lg

    def test_logo(self, monkeypatch, capsys):
        def mockreturn(fd):
            return (15, 42)

        monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
        logo()

        out, err = capsys.readouterr()

        text = (
            '\n\n\x1b[96m _ __ __ _ _ __  \x1b[0m\n' +
            "\x1b[96m| '__/ _` | '_ \\ \x1b[0m\n" +
            '\x1b[96m| | | (_| | | | |\x1b[0m\n' +
            '\x1b[96m|_|  \\__,_|_| |_|\x1b[0m\n')

        assert out == text


class TestMessage:

    def test_message_with_valid_command(self, capsys):
        message('')
        out, err = capsys.readouterr()

        assert out == 'Enter [h]elp\n'

    def test_message_with_invalid_command(self, capsys):
        message('none')
        out, err = capsys.readouterr()

        assert out == '\x1b[91mBad syntax, enter [h]elp\x1b[0m\n'


def test_stats(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 10)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    stats('')

    out, err = capsys.readouterr()

    assert out == '\n\n'


@pytest.fixture()
def workout():
    data = {
        'date': {'year': 123, 'month': 1, 'day': 12},
        'run': {
            'type': 'base',
            'duration': {
                'hour': 0,
                'minute': 50,
                'second': 0,
                'micro': 0},
            'distance': 11300
        },
        'strength': {
            'pull-ups': [
                17,
                14,
                11
            ],
            'push-ups': [
                45,
                40,
                35
            ],
            'sit-ups': [
                1000
            ]
        }
    }

    return data


@pytest.fixture()
def mockreturn():
    def mock(fd):
        return (42, 24)

    return mock


@pytest.mark.usefixtures('workout', 'mockreturn')
class TestGetDate:

    def test_get_date_with_true_cancel_arg(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = True
        (cancel, data) = get_date(cancel, workout())

        assert cancel
        assert list(data['date'].values()) == [123, 1, 12]

    def test_get_date_with_cancel_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_date(cancel, workout())

        assert cancel
        assert list(data['date'].values()) == [123, 1, 12]

    def test_get_date_with_default_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())
        t = datetime.date.today()

        cancel = False
        (cancel, data) = get_date(cancel, workout())

        assert not cancel
        assert list(data['date'].values()) == [t.year, t.month, t.day]

    def test_get_date_with_valid_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '2017-5-29')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_date(cancel, workout())

        assert not cancel
        assert list(data['date'].values()) == [2017, 5, 29]
