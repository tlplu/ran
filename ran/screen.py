from .utils import getxy


logo_str = r""" _ __ __ _ _ __
| '__/ _` | '_ \
| | | (_| | | | |
|_|  \__,_|_| |_|"""


def logo_lines():
    """ Return logo's lines. """
    lines = logo_str.split("\n")
    lines[0] += '  '
    lines[1] += ' '

    return lines


def logo():
    """ Display logo. """
    x, y = getxy()

    for i in range(2):
        print()

    for line in logo_lines():
        print(line.center(x))


def stats(cmd):
    """ Display stats. """
    x, y = getxy()
    for i in range(y - 8):
        print()


def message(cmd):
    """ Display message and prompt and return input. """
    print('Enter help')
    cmd = input('> ')

    return cmd
