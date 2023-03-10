import logging
import coloredlogs
from bot import constants


def setup():
    """Setup loggers."""

    format_str = (
        "[%(levelname)s] [%(asctime)s] [%(name)s] | [%(funcName)s:%(lineno)d] | %(message)s"
    )
    date_fmt = "%Y-%m-%d %H:%M:%S"

    root_logger = logging.getLogger()

    coloredlogs.install(
        level="DEBUG" if constants.debug else "INFO",
        logger=root_logger,
        datefmt=date_fmt,
        fmt=format_str,
    )

    logging.getLogger("nextcord").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.INFO)
