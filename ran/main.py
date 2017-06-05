import ran.screen
import ran.commands


def main():
    """ The main loop. """

    cmd = ''
    while True:
        ran.screen.logo()
        ran.commands.commands(cmd)

        if cmd in ['l', 'log']:
            cmd = ''
        else:
            ran.screen.message(cmd)
            cmd = input('> ')

        if cmd in ['q', 'quit', 'exit']:
            print('Bye!')
            break
