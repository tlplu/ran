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


def get_date(cancel, workout):
    """ Get run date. """
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
        workout['date']['year'] = date.year
        workout['date']['month'] = date.month
        workout['date']['day'] = date.day

    return (cancel, workout)


def get_type(cancel, workout):
    """ Get run type. """
    if not cancel:
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
                    break
                else:
                    logo()
                    details(workout)
                    print('Bad type, enter type of run or [c]ancel')

    return (cancel, workout)


def get_duration(cancel, workout):
    """ Get run duration. """
    if not cancel:
        logo()
        details(workout)

        print('Enter duration of run in h:m:s.ms or [c]ancel')

        while not cancel:
            dur = input('> ')

            if dur in ['c', 'cancel']:
                cancel = True
            else:
                try:
                    dur = datetime.datetime.strptime(dur, '%H:%M:%S.%f')
                    workout['run']['duration']['hour'] = dur.hour
                    workout['run']['duration']['minute'] = dur.minute
                    workout['run']['duration']['second'] = dur.second
                    workout['run']['duration']['micro'] = (
                        dur.microsecond // 10000)
                    break
                except ValueError:
                    logo()
                    details(workout)
                    print('Bad format, enter duration in h:m:s.ms format')

    return (cancel, workout)


def get_distance(cancel, workout):
    """ Get run distance. """
    if not cancel:
        logo()
        details(workout)

        print('Enter distance of run (meters) or [c]ancel')

        while not cancel:
            m = input('> ')

            if m in ['c', 'cancel']:
                cancel = True
            else:
                try:
                    m = int(m)
                    if m > 0:
                        workout['run']['distance'] = m
                        break
                    else:
                        raise ValueError
                except ValueError:
                    logo()
                    details(workout)
                    print('Bad format, enter distance (positive integer)')

    return (cancel, workout)


def get_sets(cancel, workout, s):
    """ Get sets. """
    if not cancel:
        logo()
        details(workout)

        print('Enter', s, '(e.g. "10, 8, 6" for 3 sets) or [c]ancel')

        while not cancel:
            ups = input('> ')

            if ups in ['c', 'cancel']:
                cancel = True
            else:
                try:
                    ups = ups.split(', ')
                    ups = [int(x) for x in ups]
                    for x in ups:
                        if x <= 0:
                            raise ValueError

                    workout['strength'][s] = ups
                    break
                except ValueError:
                    logo()
                    details(workout)
                    print('Bad format, enter', s, '(e.g. "5, 4, 3, ...")')

    return (cancel, workout)


def get_run_strength(cancel, workout, f):
    if not cancel:
        logo()
        details(workout)

        if f == 1:
            print('Did you run? [y]es, [n]o or [c]ancel')
        else:
            print('Did you do strength workout? [y]es, [n]o, or [c]ancel')
        while True:
            run = input('> ')
            if run in ['yes', 'y', 'no', 'n', 'cancel', 'c']:
                if run in ['yes', 'y']:
                    if f == 1:
                        (cancel, workout) = get_type(cancel, workout)
                        (cancel, workout) = get_duration(cancel, workout)
                        (cancel, workout) = get_distance(cancel, workout)
                    else:
                        (cancel, workout) = get_sets(
                            cancel,
                            workout,
                            'pull-ups')
                        (cancel, workout) = get_sets(
                            cancel,
                            workout,
                            'push-ups')
                        (cancel, workout) = get_sets(
                            cancel,
                            workout,
                            'sit-ups')

                elif run in ['cancel', 'c']:
                    cancel = True
                break
            else:
                logo()
                details(workout)
                if f == 1:
                    print('Bad format. Did you run? [y]es or [n]o or [c]ancel')
                else:
                    print(
                        'Bad format. Did you do strength workout?',
                        '[y]es, [n]o, [c]ancel')

    return (cancel, workout)


def date_dict_to_str(date):
    """ Return date str. """
    if date['year'] != '':
        return (
            str(date['year']) +
            '-' +
            str(date['month']) +
            '-' +
            str(date['day']))
    else:
        return ''


def duration_dict_to_str(dur):
    """ Return duration str. """
    if dur['hour'] != '':
        return (
            str(dur['hour']) +
            ':' +
            str(dur['minute']) +
            ':' +
            str(dur['second']) +
            '.' +
            str(dur['micro']))
    else:
        return ''


def details(workout):
    """ Display workouts details. """
    x, y = getxy()

    for i in range(y - 22):
        print()

    print('\t ' + underline(color('green', 'Workout details')))
    print()
    print(
        '\t\t ' + color('green', 'Date ') +
        '\t' + date_dict_to_str(workout['date']))
    print('\t\t ' + color('green', 'Run '))
    print(
        '\t\t   ' + color('green', 'type:') +
        '\t' + workout['run']['type'])
    print(
        '\t\t   ' + color('green', 'duration: ') +
        '\t' + duration_dict_to_str(workout['run']['duration']))
    print(
        '\t\t   ' + color('green', 'distance: ') +
        '\t' + str(workout['run']['distance']))
    print('\t\t ' + color('green', 'Strength '))
    print(
        '\t\t   ' + color('green', 'pull-ups: ') +
        '\t' + str(workout['strength']['pull-ups']))
    print(
        '\t\t   ' + color('green', 'push-ups: ') +
        '\t' + str(workout['strength']['push-ups']))
    print(
        '\t\t   ' + color('green', 'sit-ups: ') +
        '\t' + str(workout['strength']['sit-ups']))

    for i in range(3):
        print()
