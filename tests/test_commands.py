import os
import pytest
import ran.commands

from ran.commands import hlp, commands, stats


def test_hlp(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 17)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    hlp()

    out, err = capsys.readouterr()
    text = (
        '\n\t \x1b[4;93mHelp\x1b[0m\n\n' +
        '\t Commands:\n' +
        '\t\t \x1b[93mh, help\x1b[0m - display this help text\n' +
        '\t\t \x1b[93mq, quit\x1b[0m - exit ran\n\n\n\n')

    assert out == text


def test_stats(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 10)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    stats('')

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
        commands(helps)

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
        commands(logs)

        out, err = capsys.readouterr()

        assert out == 'log\n'

    def test_commands_with_default_arg(self, monkeypatch, capsys):
        def mockreturn(cmd):
            print(cmd)

        monkeypatch.setattr(ran.commands, 'stats', mockreturn)
        commands('42')

        out, err = capsys.readouterr()

        assert out == '42\n'
