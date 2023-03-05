import asyncio
import os

import redis
from dotenv import load_dotenv
import nextcord
from bot.bot import ZomboBot

load_dotenv()

TEST_GUILD_ID = 1076694244271587490


async def _create_redis_connection():
    return redis.Redis(host="localhost", port=6379)


async def main():
    async with ZomboBot(await _create_redis_connection(), intents=nextcord.Intents.all()) as bot:
        @bot.slash_command(
            description="This command repeats what you tell it.", guild_ids=[TEST_GUILD_ID]
        )
        async def echo(interaction: nextcord.Interaction, content: str):
            await interaction.send(content)

        await bot.start(os.getenv("TOKEN"))


asyncio.run(main())
