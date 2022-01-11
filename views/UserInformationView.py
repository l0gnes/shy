import disnake
from disnake.components import ActionRow

from .UserInformationButtons.TimeoutUserButton import TimeoutUserButton
from .UserInformationButtons.KickUserButton import KickUserButton

class UserInformationView(disnake.ui.View):
    def __init__(self, executor : disnake.Member, user : disnake.Member, *args, **kwargs):
        super().__init__()
        self.user = user
        self.executor = executor

        if self.executor.guild_permissions.moderate_members:
            super().add_item(TimeoutUserButton(self.executor, self.user))

        if self.executor.guild_permissions.kick_members:
            super().add_item(KickUserButton(self.executor, self.user))

        if self.executor.guild_permissions.ban_members:
            return # TODO(boop): Implement the ban button 

    @disnake.ui.button(
        label = "Game Statistics",
        disabled = True,
        style = disnake.ButtonStyle.grey,
        emoji = "<:gaming:927695145439211520>"
    )
    async def fetchUserGameStatistics(self, button, interaction):
        raise NotImplementedError
