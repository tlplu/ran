from ran.screen import logo_lines


def test_logo_lines():
    lg = [
        ' _ __ __ _ _ __  ',
        "| '__/ _` | '_ \\ ",
        '| | | (_| | | | |',
        '|_|  \\__,_|_| |_|']

    assert logo_lines() == lg
