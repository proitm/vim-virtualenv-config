import sys
import vim
import os

CONFIG_FILE_NAME = '.virtualenv_config'


def __find_config_file(current_dir):
    """
    Returns path to configuration file located in the closest parent dir if
    it exists.
    Returns None otherwise.
    """
    path = current_dir
    found = None

    while True:
        _try = os.path.join(path, CONFIG_FILE_NAME)
        if os.path.isfile(_try):
            found = _try
            break
        if os.path.dirname(path) == path:
            break
        path = os.path.dirname(path)
    return found


def activate_virtualenv():
    """
    Root function which tries to activate virtualenv.
    """
    current_dir = os.getcwd()
    config_file = __find_config_file(current_dir)
    # Return if config_file wasn't found
    if not config_file:
        return
    # Try to open config file
    with open(config_file, 'r') as config:
        # Read virtualenv dir path from config file
        virtualenv_path = config.read().replace('\n', '')
        # Check if virtualenv dir exists
        if os.path.isdir(virtualenv_path):
            # Make path to activate_this.py file
            activate_this = \
                os.path.join(virtualenv_path, 'bin', 'activate_this.py')
            if os.path.isfile(activate_this):
                # Finally activate virtual environment for vim
                sys.path.insert(0, virtualenv_path)
                execfile(activate_this, dict(__file__=activate_this))


def initPythonModule():
    if sys.version_info[:2] < (2, 4):
        vim.command('let s:has_supported_python = 0')
        return
    # Try to activate virtualenv
    activate_virtualenv()
