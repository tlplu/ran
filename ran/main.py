from .screen import logo, message
from .commands import commands


def main():
    """ The main loop. """

    cmd = ''
    while True:
        logo()
        commands(cmd)
        cmd = message(cmd)

        if cmd in ['q', 'quit', 'exit']:
            print('Bye!')
            break
