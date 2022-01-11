import disnake
from disnake.ext import commands

class ShyContext(disnake.ApplicationCommandInteraction):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args, **kwargs
        )

    async def quickEmbed(self, *args, **kwargs):
        col = kwargs.pop("colour", 0xFFFFFE)
        return await super().send(
            embed = disnake.Embed(
                colour = col,
                *args, **kwargs
            )
        )