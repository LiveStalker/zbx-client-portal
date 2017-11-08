import os
from os.path import join, dirname, abspath
from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name, default=None):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        if not default:
            error_msg = 'Set the {} environment variable'.format(var_name)
            raise ImproperlyConfigured(error_msg)
        else:
            return default


def root(*dirs):
    base_dir = join(dirname(__file__), '..', '..')
    return abspath(join(base_dir, *dirs))
