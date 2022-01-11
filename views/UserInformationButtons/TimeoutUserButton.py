import disnake
from ..TimeoutUserView import TimeoutUserView

class TimeoutUserButton(disnake.ui.Button):
    def __init__(self, executor : disnake.Member, user : disnake.Member, *args, **kwargs):
        super().__init__(
            style = disnake.ButtonStyle.danger,
            label = "Timeout User",
            emoji = "<:mute:927697791675949126>",
            row = 1
        )

        self.user = user
        self.executor = executor

        if not executor.guild_permissions.moderate_members:
            super().disabled = True

    async def callback(self, interaction : disnake.MessageInteraction):
        return await interaction.send(
            embed = disnake.Embed(
                colour = 0xEAEAEA,
                description = "If you need a more specific time, use the `/timeout` command."
            ).set_author(
                name = "Please choose an option below",
                icon_url = interaction.author.avatar
            ),
            view = TimeoutUserView(
                self.executor,
                self.user
            ),
            ephemeral = True
        )



