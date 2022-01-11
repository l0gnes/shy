import disnake

class KickUserButton(disnake.ui.Button):
    def __init__(self, executor : disnake.Member, user : disnake.Member, *args, **kwargs):
        super().__init__(
            label = "Kick User",
            emoji = "<:boot:927705619870388234>",
            style = disnake.ButtonStyle.red,
            row = 1
        )

        self.executor = executor
        self.user = user

    async def callback(self, interaction : disnake.MessageInteraction):
        return