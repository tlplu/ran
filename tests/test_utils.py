import os

from ran.utils import getxy


def test_getxy(monkeypatch):
    def mockreturn(fd):
        return (42, 24)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    x, y = getxy()

    assert (x, y) == (42, 24)
