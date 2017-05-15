from ran.color import color, underline


class TestColor:

    def test_black(self):
        assert color('black', 'test') == '\x1b[90mtest\x1b[0m'

    def test_red(self):
        assert color('red', 'test') == '\x1b[91mtest\x1b[0m'

    def test_green(self):
        assert color('green', 'test') == '\x1b[92mtest\x1b[0m'

    def test_yellow(self):
        assert color('yellow', 'test') == '\x1b[93mtest\x1b[0m'

    def test_blue(self):
        assert color('blue', 'test') == '\x1b[94mtest\x1b[0m'

    def test_purple(self):
        assert color('purple', 'test') == '\x1b[95mtest\x1b[0m'

    def test_cyan(self):
        assert color('cyan', 'test') == '\x1b[96mtest\x1b[0m'


class TestUnderline:

    def test_underline(self):
        assert underline('\x1b[96mtest\x1b[0m') == '\x1b[4;96mtest\x1b[0m'
