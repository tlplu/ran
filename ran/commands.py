from .screen import hlp, stats


def commands(cmd):
    """ Call the proper function. """
    if cmd in ['h', 'help']:
        hlp()

    else:
        stats(cmd)
