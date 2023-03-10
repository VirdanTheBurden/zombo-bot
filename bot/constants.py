import logging
import os

from dotenv import load_dotenv
import yaml
import pathlib


load_dotenv()
logger = logging.getLogger(__name__)


# allow for ENV constructor
def _load_env_vars(loader, node):
    default = None

    if node.id == "scalar":
        # 'tis the key
        value = loader.construct_scalar(node)
        key = value

    else:
        # 'tis the list of legend
        value = loader.construct_sequence(node)
        if len(value) > 2 or len(value) < 0:
            raise AttributeError(
                f"There can be at most 2 items or at least 1 item. There are {len(value)} present."
            )

        elif len(value) == 2:
            # key and default
            key, default = value

        else:
            # just the one
            (key,) = value

    return os.getenv(key, default)


# create getter metaclass
class YAMLAccessor(type):
    """Allows for access of YAML config data via class attributes.
    Thanks to PyDis for the idea and implementation.
    """

    subsection = None

    def __getattr__(cls, name):
        name = name.lower()
        entry = ".".join(
            (cls.section, cls.subsection, name)
            if cls.subsection is not None
            else (cls.section, name)
        )

        try:
            logger.debug(f"Attempting to access entry {entry}...")
            if cls.subsection is not None:
                return _YAML_DATA[cls.section][cls.subsection][name]
            return _YAML_DATA[cls.section][name]
        except KeyError as e:
            raise AttributeError(f"Entry {entry} does not exist.") from e

    def __getitem__(cls, name):
        return cls.__getattr__(name)


# load on custom builders
yaml.SafeLoader.add_constructor("!ENV", _load_env_vars)

# get the data
with open(pathlib.Path("config.yml")) as f:
    _YAML_DATA = yaml.safe_load(f)

# set non-nested data
debug: bool = _YAML_DATA["debug"]
file_logs: bool = _YAML_DATA["file_logs"]


# set up nested data
class Bot(metaclass=YAMLAccessor):
    section = "bot"

    prefix: str
    token: str


class Guild(metaclass=YAMLAccessor):
    section = "guild"

    id: int


class Categories(metaclass=YAMLAccessor):
    section = "guild"
    subsection = "categories"

    team_voicechannels: int


class Channels(metaclass=YAMLAccessor):
    section = "guild"
    subsection = "channels"

    bot_log: int
    team_log: int
    server_status_log: int
