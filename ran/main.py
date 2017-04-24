from .screen import logo, stats, message
from .config import get_data_file


def main():
    """ The main loop. """
    data = get_data_file()

    cmd = ''
    while True:
        logo()
        stats(cmd)
        cmd = message(cmd)

