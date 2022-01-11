import disnake
from typing import Optional

class HelpView(disnake.ui.View):
    def __init__(self, interaction, *, timeout: Optional[float] = 180):
        self.interaction = interaction 
        super().__init__(timeout=timeout)

        self.current_category = None
        self.current_help_page = 0
        self.max_help_pages = 0

        super().add_item(
            disnake.ui.Select(
                custom_id="category_select",
                options = [
                    disnake.SelectOption(
                        label = c.name
                    ) for c in self.interaction.bot.cogs
                ]
            )
        )

    @disnake.ui.button(
        label = "Previous",
        custom_id="previous_button",
        disabled=True,
        style = disnake.ButtonStyle.blurple
    )
    async def _previousHelpPage(self, button, interaction):
        self.current_help_page -= 1


    