import disnake
from datetime import timedelta

class TimeoutUserView(disnake.ui.View):
    def __init__(self, executor : disnake.Member, user : disnake.Member, *args, **kwargs):
        super().__init__()

        self.executor = executor
        self.user = user

    def _ensureTimeoutPermissions(self) -> bool:
        return self.executor.guild_permissions.moderate_members

    @disnake.ui.button(
        label = "Timeout 5m",
        style = disnake.ButtonStyle.danger,
    )
    async def timeoutUser5Minutes(self, button, interaction):

        if self._ensureTimeoutPermissions():
            await self.user.timeout(
                duration = timedelta(
                    minutes = 5
                )
            )

            return await interaction.send(
                embed = disnake.Embed(
                    colour = 0xEAEAEA,
                    description = f"<:mute:927697791675949126> {self.user.mention} has been timed out for 5 minutes."
                ),
                ephemeral = True
            )

    @disnake.ui.button(
        label = "Timeout 15m",
        style = disnake.ButtonStyle.danger,
    )
    async def timeoutUser15Minutes(self, button, interaction):

        if self._ensureTimeoutPermissions():
            await self.user.timeout(
                duration = timedelta(
                    minutes = 15
                )
            )

            return await interaction.send(
                embed = disnake.Embed(
                    colour = 0xEAEAEA,
                    description = f"<:mute:927697791675949126> {self.user.mention} has been timed out for 15 minutes."
                ),
                ephemeral = True
            )

    @disnake.ui.button(
        label = "Timeout 1h",
        style = disnake.ButtonStyle.danger,
    )
    async def timeoutUser1Hour(self, button, interaction):

        if self._ensureTimeoutPermissions():
            await self.user.timeout(
                duration = timedelta(
                    hours = 1
                )
            )

            return await interaction.send(
                embed = disnake.Embed(
                    colour = 0xEAEAEA,
                    description = f"<:mute:927697791675949126> {self.user.mention} has been timed out for 1 hour."
                ),
                ephemeral = True
            )

    @disnake.ui.button(
        label = "Timeout 12h",
        style = disnake.ButtonStyle.danger,
    )
    async def timeoutUser12Hours(self, button, interaction):

        if self._ensureTimeoutPermissions():
            await self.user.timeout(
                duration = timedelta(
                    hours = 12
                )
            )

            return await interaction.send(
                embed = disnake.Embed(
                    colour = 0xEAEAEA,
                    description = f"<:mute:927697791675949126> {self.user.mention} has been timed out for 12 hours."
                ),
                ephemeral = True
            )

    @disnake.ui.button(
        label = "Timeout 24h",
        style = disnake.ButtonStyle.danger,
    )
    async def timeoutUser24Hours(self, button, interaction):

        if self._ensureTimeoutPermissions():
            await self.user.timeout(
                duration = timedelta(
                    days = 1
                )
            )

            return await interaction.send(
                embed = disnake.Embed(
                    colour = 0xEAEAEA,
                    description = f"<:mute:927697791675949126> {self.user.mention} has been timed out for 24 hours."
                ),
                ephemeral = True
            )