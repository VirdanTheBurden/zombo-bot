import asyncio
import os

import nextcord
import redis.asyncio as redis
from dotenv import load_dotenv

from bot.bot import ZomboBot


load_dotenv()


async def main():
    async with ZomboBot(redis.Redis(host="localhost", port=6379), intents=nextcord.Intents.all()) as _bot:
        await _bot.start(os.getenv("TOKEN"))

if __name__ == "__main__":
    asyncio.run(main())
