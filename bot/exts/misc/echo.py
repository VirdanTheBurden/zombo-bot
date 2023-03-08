import nextcord
from nextcord.ext import commands

TEST_GUILD_ID = 1076694244271587490


class Echo(commands.Cog):
    def __init__(self, _bot):
        self._bot = _bot

    @nextcord.slash_command(
        description="This command repeats what you tell it.", guild_ids=[TEST_GUILD_ID]
    )
    async def echo(self, interaction: nextcord.Interaction, content: str):
        await interaction.send(content)


def setup(bot: commands.Bot):
    print("Echo cog is being loaded.")
    bot.add_cog(Echo(bot))
