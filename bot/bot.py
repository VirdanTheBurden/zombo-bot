import logging
import pathlib

import redis.asyncio as redis
from nextcord.ext import commands

logger = logging.getLogger(__name__)

TEST_GUILD_ID = 1076694244271587490


class ZomboBot(commands.Bot):
    """
    Subclass of ``nextcord.ext.commands.Bot`` that implements an attribute
    for connection to a redis database.
    """

    def __init__(self, redis_conn: redis.Redis, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._redis = redis_conn

    @staticmethod
    def get_extensions():
        p = pathlib.Path.cwd() / "bot"

        for path in p.glob("exts/**/*.py"):
            if "__init__" in str(path):
                continue
            ext = ".".join(path.parts[2:]).strip(".py")
            logger.info(f"Loading {ext[4:]}...")
            yield ext

    async def __aenter__(self):
        self.load_extensions(list(self.get_extensions()))
        logger.info("All extensions loaded.")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._redis.bgsave()
        logger.info("Closing redis session.")
        await self._redis.close()

        if isinstance(KeyboardInterrupt, exc_val):
            return True

        return False
