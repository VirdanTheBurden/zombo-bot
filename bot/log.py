import logging
import coloredlogs
from bot import constants

def setup():
    """Setup loggers."""

    format_str = "[%(asctime)s] [%(levelname)-8s] [%(name)-36s] | [%(funcName)20s:%(lineno)-5d] | %(message)s"
    date_fmt = "%Y-%m-%d %H:%M:%S"

    root_logger = logging.getLogger()

    coloredlogs.install(
        level="DEBUG" if constants.debug else "INFO",
        logger=root_logger,
        fmt=format_str,
        datefmt=date_fmt

    )

    logging.getLogger("nextcord").setLevel(logging.WARNING)
    logging.getLogger("asyncio").setLevel(logging.INFO)
