import disnake
from disnake.ext import commands
from utils.nekosApiWrapper import ShyNekosAPI
from ..cogtemplate import Cog

class ReactionCommands(Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.slash_command(
        name = "hug",
        description = "Hug somebody, or maybe even yourself!"
    )
    async def reactHugCommand(
        self,
        interaction,
        user : disnake.Member = None
    ):
        hug_gif = await ShyNekosAPI.hug()

        if user is None or user == interaction.author:
            return await interaction.send(
                embed = disnake.Embed(
                    description = f"🤍 {interaction.author.mention} hugged themself!"
                ).set_image(
                    url = hug_gif
                )
            )

        return await interaction.send(
            embed = disnake.Embed(
                colour = 0xeaeaea,
                description = f"🤍 {interaction.author.mention} hugged {user.mention}!"
            ).set_image(
                url = hug_gif
            )
        )

    @commands.slash_command(
        name = "kiss",
        description = "Kiss somebody, or maybe even yourself!"
    )
    async def reactKissCommand(
        self,
        interaction,
        user : disnake.Member = None
    ):
        kiss_gif = await ShyNekosAPI.kiss()

        if user is None or user == interaction.author:
            return await interaction.send(
                embed = disnake.Embed(
                    description = f"🤍 {interaction.author.mention} kissed themself!"
                ).set_image(
                    url = kiss_gif
                )
            )

        return await interaction.send(
            embed = disnake.Embed(
                colour = 0xeaeaea,
                description = f"🤍 {interaction.author.mention} kissed {user.mention}!"
            ).set_image(
                url = kiss_gif
            )
        )

    @commands.slash_command(
        name = "pat",
        description = "Pat somebody, or maybe even yourself!"
    )
    async def reactPatCommand(
        self,
        interaction,
        user : disnake.Member = None
    ):
        pet_gif = await ShyNekosAPI.pat()

        if user is None or user == interaction.author:
            return await interaction.send(
                embed = disnake.Embed(
                    description = f"🤍 {interaction.author.mention} patted themself!"
                ).set_image(
                    url = pet_gif
                )
            )

        return await interaction.send(
            embed = disnake.Embed(
                colour = 0xeaeaea,
                description = f"🤍 {interaction.author.mention} patted {user.mention}!"
            ).set_image(
                url = pet_gif
            )
        )