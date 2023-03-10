import asyncio
import logging

from bot import constants

import nextcord
import redis.asyncio as redis

from bot.bot import ZomboBot
from bot import log


log.setup()


async def main():
    async with ZomboBot(
        redis.Redis(host="localhost", port=6379), intents=nextcord.Intents.all(),
        command_prefix=constants.Bot.prefix
    ) as _bot:
        await _bot.start(constants.Bot.token)


if __name__ == "__main__":
    asyncio.run(main())
