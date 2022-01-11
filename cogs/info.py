import disnake
from disnake.ext import commands
from disnake.ext.commands.params import Param
from typing import Union

from disnake.interactions.application_command import ApplicationCommandInteraction

from views.BotInformationView import BotInformationView  
from views.UserInformationView import UserInformationView
from embeds.BotInformationEmbed import BotInformationEmbed

class InformationCog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name="bot",
        description="Shows information about the bot."
    )
    async def _botInformationCommand(self, interaction):

        view = BotInformationView(interaction)

        view.MESSAGE = await interaction.send(
            embed=BotInformationEmbed(interaction),
            view = view,
            ephemeral = True
        )

    @commands.slash_command(
        name="user",
        description="Shows user information"
    )
    async def _userInformationCommand(self, interaction : ApplicationCommandInteraction, user : disnake.User):

        userInformationEmbed = disnake.Embed(
            colour = 0xEAEAEA
        )

        userInformationEmbed.set_author(name = f"user info: {str(user)}")
        userInformationEmbed.set_thumbnail(url = user.avatar or user.default_avatar)

        if hasattr(user, "guild"):
            pass

        return await interaction.send(
            ephemeral = True,
            embed = userInformationEmbed,
            view = UserInformationView(interaction.author, user)
        )

def setup(client):
    client.add_cog(
        InformationCog(client)
    )