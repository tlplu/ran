def color(clr, txt):
    """ Return colorful text. """
    colors = {
        'black': '\x1b[90m',
        'red': '\x1b[91m',
        'green': '\x1b[92m',
        'yellow': '\x1b[93m',
        'blue': '\x1b[94m',
        'purple': '\x1b[95m',
        'cyan': '\x1b[96m',
    }

    return colors[clr] + txt + '\x1b[0m'


def underline(ctxt):
    """ Underline colorful text. """
    return ctxt[0:2] + '4;' + ctxt[2:]
