from ran.screen import logo_lines
from ran.screen import message


def test_logo_lines():
    lg = [
        ' _ __ __ _ _ __  ',
        "| '__/ _` | '_ \\ ",
        '| | | (_| | | | |',
        '|_|  \\__,_|_| |_|']

    assert logo_lines() == lg


class TestMessage:

    def test_message_with_valid_command(self, capsys):
        message('')
        out, err = capsys.readouterr()

        assert out == 'Enter [h]elp\n'

    def test_message_with_invalid_command(self, capsys):
        message('none')
        out, err = capsys.readouterr()

        assert out == '\x1b[91mBad syntax, enter [h]elp\x1b[0m\n'
