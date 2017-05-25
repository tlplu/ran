import os

from ran.screen import logo_lines, message, logo


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
