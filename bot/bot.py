import redis
from nextcord.ext import commands


class ZomboBot(commands.Bot):
    def __init__(self, redis_conn: redis.Redis, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._redis = redis_conn

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        self._redis.save()

        if isinstance(KeyboardInterrupt, exc_val):
            return True

        return False
