# train-project/train_schedule/config.py
from pathlib import Path

from platformdirs import user_config_dir
from pydantic import BaseSettings

from . import APP_NAME

CONFIG_FILENAME = "config.json"


class Config(BaseSettings):
    """The app configuration"""

    api_url: str = ""


def load_config():
    """Load the app configuration

    Load the configuration from the user config file. If there's
    an error reading from the file (e.g. if it doesn't exist) use
    the default config values."""
    cfg_path = get_config_path()
    try:
        return Config.parse_file(cfg_path)
    except IOError:
        return Config()


def save_config(config):
    """Save the configuration

    Save the current configuration to the user config file. Only
    write config values which have explicitly been set, and are
    different from the defaults."""
    cfg_path = get_config_path()
    ensure_dir_exists(cfg_path.parent)

    cfg = config.json(exclude_defaults=True, exclude_unset=True)

    with open(cfg_path, "w") as stream:
        stream.write(cfg)


def get_config_path():
    """Get the path to the config file

    Get the (platform specific) path to the user configuration
    file for our application"""
    config_dir = Path(user_config_dir(APP_NAME)).resolve()
    return config_dir / CONFIG_FILENAME


def ensure_dir_exists(path):
    """Make sure the config directory exists

    If the directory doesn't exist create it (and all its ancestor
    directories)"""
    if not path.is_dir():
        path.mkdir(parents=True)
