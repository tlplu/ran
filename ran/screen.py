import datetime

from .utils import getxy
from .color import color, underline


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
        print(color('cyan', line.center(x)))


def stats(cmd):
    """ Display stats. """
    x, y = getxy()
    for i in range(y - 8):
        print()


def message(cmd):
    """ Display message and prompt and return input. """
    if cmd not in ['', 'h', 'help']:
        print(color('red', 'Bad syntax, enter [h]elp'))
    else:
        print('Enter [h]elp')

    cmd = input('> ')

    return cmd


def hlp():
    """ Display help. """
    x, y = getxy()

    for i in range(y - 16):
        print()

    print('\t ' + underline(color('yellow', 'Help')))
    print()
    print('\t Commands:')
    print('\t\t ' + color('yellow', 'h, help') + ' - display this help text')
    print('\t\t ' + color('yellow', 'q, quit') + ' - exit ran')

    for i in range(3):
        print()


def log():
    """ Log workout. """

    def details(workout):
        """ Display workouts details"""
        for i in range(y - 22):
            print()

        print('\t ' + underline(color('green', 'Workout details')))
        print()
        print('\t\t ' + color('green', 'date: ') + workout['date'])
        print('\t\t ' + color('green', 'run: '))
        print(
            '\t\t   ' + color('green', 'type:') +
            '\t' + workout['run']['type'])
        print(
            '\t\t   ' + color('green', 'duration: ') +
            '\t' + workout['run']['duration'])
        print(
            '\t\t   ' + color('green', 'distance: ') +
            '\t' + workout['run']['distance'])
        print('\t\t ' + color('green', 'strength: '))
        print(
            '\t\t   ' + color('green', 'pull-ups: ') +
            '\t' + workout['strength']['pull-ups'])
        print(
            '\t\t   ' + color('green', 'push-ups: ') +
            '\t' + workout['strength']['push-ups'])
        print(
            '\t\t   ' + color('green', 'abs: ') +
            '\t' + workout['strength']['abs'])

        for i in range(3):
            print()

    x, y = getxy()
    workout = {
        'date': '',
        'run': {'type': '', 'duration': '', 'distance': ''},
        'strength': {'pull-ups': '', 'push-ups': '', 'abs': ''}
    }
    cancel = False

    details(workout)
    print('Enter date in YYYY-mm-dd format (default today) or [c]ancel')

    while not cancel:
        date = input('> ')

        if date in ['c', 'cancel']:
            cancel = True
        else:
            if date == '':
                date = datetime.date.today()
                break
            else:
                try:
                    date = datetime.datetime.strptime(date, '%Y-%m-%d')
                    break
                except ValueError:
                    logo()
                    details(workout)
                    print('Bad format, enter date in YYYY-mm-dd format')

    if not cancel:
        workout['date'] = date.strftime('%Y-%m-%d')

        logo()
        details(workout)

        print('Enter type of run (default base) or [c]ancel')

        while not cancel:
            run = input('> ')

            if run in ['c', 'cancel']:
                cancel = True
            else:
                if run in ['base', '']:
                    workout['run']['type'] = 'base'
                    logo()
                    details(workout)
                    break
                else:
                    logo()
                    details(workout)
                    print('Bad type, enter type of run or [c]ancel')
