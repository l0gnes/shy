import disnake

class BotInformationEmbed(disnake.Embed):
    def __init__(self, inter : disnake.ApplicationCommandInteraction, *args, **kwargs):
        self.interaction = inter

        super().__init__(
            colour = 0xEAEAEA,
            description = """shy is a minimalistic bot which only provides unique experiences. This bot's expectation is that it should bring a feature set which is useful to your server that isn't offered my any other bot out there."""
        )

        super().set_author(
            name = "shy, a niche minimalistic discord bot.",
            icon_url = self.interaction.bot.user.avatar
        )

        super().set_footer(
            text = "🤍 shy is being programmed and maintained by boop#9092"
        )