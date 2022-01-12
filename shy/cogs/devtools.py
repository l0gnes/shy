import disnake
from disnake.ext import commands
from traceback import format_exception
from utils.funcs import (
    quickDefer,
    fetchAllAvailableCogs
)

class DeveloperTools(commands.Cog):
    def __init__(self, client : commands.AutoShardedBot):
        self.client = client

    @commands.slash_command(
        name = "reload",
        description = "Reloads bot cogs"
    )
    @commands.is_owner()
    async def _devtoolsReload(
        self,
        interaction : disnake.ApplicationCommandInteraction, 
        cog : str = commands.Param(choices=fetchAllAvailableCogs())
    ):
        await quickDefer(interaction)

        if cog.startswith("cogs."):
            cog = cog.split(".").pop(0)
            cog = ".".join(cog)

        try:
            self.client.reload_extension(
                f"cogs.{cog}" if not cog.startswith("cogs.") else cog
            )
        except Exception as exc:
            error = format_exception(exc)
            return await interaction.send(
                f"```py\n{error}```"
            )
        else:
            return await interaction.send(
                f"`{cog}` was reloaded!"
            )

    @commands.slash_command(
        name = "load",
        description = "Loads bot cogs"
    )
    @commands.is_owner()
    async def _devtoolsLoad(
        self,
        interaction : disnake.ApplicationCommandInteraction, 
        cog : str = commands.Param(choices=fetchAllAvailableCogs())
    ):
        await quickDefer(interaction)

        if cog.startswith("cogs."):
            cog = cog.split(".").pop(0)
            cog = ".".join(cog)

        try:
            self.client.load_extension(
                f"cogs.{cog}" if not cog.startswith("cogs.") else cog
            )
        except Exception as exc:
            error = format_exception(exc)
            return await interaction.send(
                f"```py\n{error}```"
            )
        else:
            return await interaction.send(
                f"`{cog}` was loaded!"
            )

    @commands.slash_command(
        name = "unload",
        description = "Unloads bot cogs"
    )
    @commands.is_owner()
    async def _devtoolsUnload(
        self,
        interaction : disnake.ApplicationCommandInteraction, 
        cog : str = commands.Param(choices=fetchAllAvailableCogs())
    ):
        await quickDefer(interaction)

        if cog.startswith("cogs."):
            cog = cog.split(".").pop(0)
            cog = ".".join(cog)

        try:
            self.client.unload_extension(
                f"cogs.{cog}" if not cog.startswith("cogs.") else cog
            )
        except Exception as exc:
            error = format_exception(exc)
            return await interaction.send(
                f"```py\n{error}```"
            )
        else:
            return await interaction.send(
                f"`{cog}` was unloaded!"
            )

def setup(client):
    client.add_cog(
        DeveloperTools(
            client
        )
    )