import ran.color


class TestColor:

    def test_black(self):
        assert ran.color.color('black', 'test') == '\x1b[90mtest\x1b[0m'

    def test_red(self):
        assert ran.color.color('red', 'test') == '\x1b[91mtest\x1b[0m'

    def test_green(self):
        assert ran.color.color('green', 'test') == '\x1b[92mtest\x1b[0m'

    def test_yellow(self):
        assert ran.color.color('yellow', 'test') == '\x1b[93mtest\x1b[0m'

    def test_blue(self):
        assert ran.color.color('blue', 'test') == '\x1b[94mtest\x1b[0m'

    def test_purple(self):
        assert ran.color.color('purple', 'test') == '\x1b[95mtest\x1b[0m'

    def test_cyan(self):
        assert ran.color.color('cyan', 'test') == '\x1b[96mtest\x1b[0m'


class TestUnderline:

    def test_underline(self):
        assert ran.color.underline('\x1b[96mtest\x1b[0m') == (
                '\x1b[4;96mtest\x1b[0m')
