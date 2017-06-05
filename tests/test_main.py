import pytest

import ran.main


class TestMain:

    @pytest.fixture(params=['q', 'quit', 'exit'])
    def end(self, request):
        return request.param

    def test_main_with_exit_commands(self, monkeypatch, capsys, end):
        monkeypatch.setattr(ran.commands, 'commands', lambda x: None)
        monkeypatch.setattr(ran.screen, 'logo', lambda: None)
        monkeypatch.setattr(ran.screen, 'message', lambda x: None)
        monkeypatch.setitem(__builtins__, 'input', lambda x: end)
        ran.main.main()

        out, err = capsys.readouterr()

        assert out == 'Bye!\n'
