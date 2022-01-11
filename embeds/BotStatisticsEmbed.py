import disnake
from inspect import cleandoc

class BotStatisticsEmbed(disnake.Embed):
    def __init__(self, inter, *args, **kwargs):
        super().__init__(
            colour = 0xeaeaea
        )

        super().set_author(
            icon_url = inter.bot.user.avatar,
            name = "shy's statistics"
        )

        super().add_field(
            name = "\u200b",
            value=cleandoc(f"""
            <:puzzle:927382279897100288> Shards: `{inter.bot.shard_count}`
            <:shield:927383034867642389> Guilds: `{len(inter.bot.guilds):,}`
            <:users:927383451282337802> Users: `{len(set(inter.bot.get_all_members())):,}`
            <:command:927383824877387868> Commands: `{len(inter.bot.slash_commands)}`
            <:cog:927383825158393866> Cogs: `{len(inter.bot.cogs)}`
            """)
        )