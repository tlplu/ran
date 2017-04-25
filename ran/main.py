from .screen import logo, stats, message


def main():
    """ The main loop. """

    cmd = ''
    while True:
        logo()
        stats(cmd)
        cmd = message(cmd)
