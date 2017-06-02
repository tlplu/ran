import json

import ran.utils
import ran.color
import ran.screen
import ran.config


def hlp():
    """ Display help. """
    x, y = ran.utils.getxy()

    for i in range(y - 16):
        print()

    print('\t ' + ran.color.underline(ran.color.color('yellow', 'Help')))
    print()
    print('\t Commands:')
    print('\t\t ' + ran.color.color('yellow', 'h, help') + ' - display this help text')
    print('\t\t ' + ran.color.color('yellow', 'q, quit') + ' - exit ran')

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

    (cancel, workout) = ran.screen.get_date(cancel, workout)
    (cancel, workout) = ran.screen.get_run_strength(cancel, workout, 1)
    (cancel, workout) = ran.screen.get_run_strength(cancel, workout, 0)

    if not cancel:
        fl = ran.config.get_data_file()
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


def stats(cmd):
    """ Display stats. """
    x, y = ran.utils.getxy()
    for i in range(y - 8):
        print()


def commands(cmd):
    """ Call the proper function. """
    if cmd in ['h', 'help']:
        hlp()

    elif cmd in ['l', 'log']:
        log()

    else:
        stats(cmd)
