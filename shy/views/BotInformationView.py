from disnake import ui
import disnake
from disnake.enums import ButtonStyle 

from embeds.BotStatisticsEmbed import BotStatisticsEmbed

class BotInformationView(ui.View):

    MESSAGE : disnake.Message

    def __init__(self, inter, *args, **kwargs):
        super().__init__()
        self.interaction = inter

        self.add_item(
            ui.Button(
                label="Invite shy!", 
                url = self.interaction.bot.BOT_INVITE_URL, 
                emoji="<:link:927594539110260790>"
            )
        )

    @ui.button(
        label = "Statistics",
        emoji = "<:piechart:927594256636457000>"
    )
    async def testButton(self, button, inter):
        return await inter.send(
            embed = BotStatisticsEmbed(self.interaction),
            ephemeral = True
        )