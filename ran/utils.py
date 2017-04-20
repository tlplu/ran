import os


def getxy():
    """ Get terminal columns and lines. """
    return os.get_terminal_size(0)
