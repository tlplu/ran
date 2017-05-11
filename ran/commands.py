import json

from .utils import getxy
from .color import color, underline
from .screen import get_date, get_run_strength, stats
from .config import get_data_file


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

    workout = {
        'date': {'year': '', 'month': '', 'day': ''},
        'run': {
            'type': '',
            'duration': {
                'hour': '',
                'minute': '',
                'second': '',
                'micro': ''},
            'distance': ''},
        'strength': {'pull-ups': '', 'push-ups': '', 'sit-ups': ''}
    }
    cancel = False

    (cancel, workout) = get_date(cancel, workout)
    (cancel, workout) = get_run_strength(cancel, workout, 1)
    (cancel, workout) = get_run_strength(cancel, workout, 0)

    if not cancel:
        fl = get_data_file()
        with open(fl, 'r') as f:
            data = json.load(f)

        data['workouts'].append(workout)

        with open(fl, 'w') as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False,
                separators=(', ', ': '))


def commands(cmd):
    """ Call the proper function. """
    if cmd in ['h', 'help']:
        hlp()

    elif cmd in ['l', 'log']:
        log()

    else:
        stats(cmd)
