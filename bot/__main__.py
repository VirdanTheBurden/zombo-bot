import os
from dotenv import load_dotenv
import nextcord
from nextcord.ext import commands

load_dotenv()

TEST_GUILD_ID = 1076694244271587490

bot = commands.Bot(intents=nextcord.Intents.all())


@bot.slash_command(description="This command repeats what you tell it.", guild_ids=[TEST_GUILD_ID])
async def echo(interaction: nextcord.Interaction, content: str):
    await interaction.send(content)


bot.run(os.getenv("TOKEN"))
