import nextcord
from nextcord.ext import commands
import logging
from bot import constants

logger = logging.getLogger(__name__)


class Echo(commands.Cog):
    def __init__(self, _bot):
        self._bot = _bot

    @nextcord.slash_command(
        description="This command repeats what you tell it.",
        guild_ids=[constants.Guild.id],
    )
    async def echo(self, interaction: nextcord.Interaction, content: str):
        await interaction.send(content)


def setup(bot: commands.Bot):
    bot.add_cog(Echo(bot))
