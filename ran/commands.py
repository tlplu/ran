from .screen import hlp, stats, log


def commands(cmd):
    """ Call the proper function. """
    if cmd in ['h', 'help']:
        hlp()

    elif cmd in ['l', 'log']:
        log()

    else:
        stats(cmd)
