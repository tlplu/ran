import os

from ran.commands import hlp


def test_hlp(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 10)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    hlp()

    out, err = capsys.readouterr()
    text = (
        '\t \x1b[4;93mHelp\x1b[0m\n\n' +
        '\t Commands:\n' +
        '\t\t \x1b[93mh, help\x1b[0m - display this help text\n' +
        '\t\t \x1b[93mq, quit\x1b[0m - exit ran\n\n\n\n')

    assert out == text
