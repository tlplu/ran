import os


def get_config_dir():
    """ Get configuration dir """
    confdir = os.path.join(os.path.expanduser("~"), '.config')

    ran_confdir = os.path.join(confdir, 'ran')

    os.makedirs(ran_confdir, exist_ok=True)

    return ran_confdir


def get_data_file():
    """ Get data file """
    ran_data = os.path.join(get_config_dir(), 'data.json')

    if not os.path.exists(ran_data):
        open(ran_data, 'w').close()

    return ran_data
