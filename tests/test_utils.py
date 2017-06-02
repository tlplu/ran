import os

import ran.utils


def test_getxy(monkeypatch):
    def mockreturn(fd):
        return (42, 24)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    x, y = ran.utils.getxy()

    assert (x, y) == (42, 24)
