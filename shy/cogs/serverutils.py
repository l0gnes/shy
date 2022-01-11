import disnake
from disnake.ext import commands
import aiohttp
from sys import getsizeof

class ServerUtilities(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name = "stealemoji",
        description = "Downloads the provided emoji and adds it to the server."
    )
    @commands.has_guild_permissions(manage_emojis = True)       # Users need to have the manage emojis permission.
    @commands.bot_has_guild_permissions(manage_emojis = True)   # The bot also needs this permission to actually create the emoji.
    @commands.guild_only()                                      # This command can only be used in guilds since only it alters aspects of them.
    async def serverUtilsDownloadEmoji(
        self, 
        interaction : disnake.ApplicationCommandInteraction,
        emoji_string : str                                      # Just in case somebody tries to execute the command with a unicode emoji.
    ):

        await interaction.response.defer()                      # Defer the response to prevent timeouts and to add *pizzaz*

        emoji = disnake.PartialEmoji.from_str(emoji_string)     # PartialEmoji.from_str() parses both unicode/custom emojis.

        if emoji.is_unicode_emoji():                            # Since everybody anybody can use unicode emojis, no point in making duplicates.

            return await interaction.send(
                f"That is not a custom emoji, that is a unicode emoji. You can use it anywheres! {emoji}",
                ephemeral = True
            )
        
        if (                                                    # Ensuring that the user isn't exceeding the guild's emoji limit.
            emoji.animated and len([e for e in interaction.guild.emojis if e.animated]) == interaction.guild.emoji_limit or
            not emoji.animated and len([e for e in interaction.guild.emojis if not e.animated]) == interaction.guild.emoji_limit
            ):
            return await interaction.send(                      
                f"Oh no! It seems like you've hit your emoji limit! `({interaction.guild.emoji_limit})`",
                ephemeral = True
            )

        async with aiohttp.ClientSession() as client_session:
            async with client_session.get(emoji.url) as emoji_response:
                emojiBytes = await emoji_response.read()                                # We need the bytes of the image for whatever reason.

        if getsizeof(emojiBytes) > 256000:                                              # This technically shouldn't happen, but let the user know if somehow ...
            return await interaction.send(                                              # ... the size of the emoji is too large.
                "It seems like the file is too big for some reason?",
                ephemeral = True
            )

        clonedEmoji = await interaction.guild.create_custom_emoji(
            name = emoji.name,
            image = emojiBytes,
            reason = f"Added by user: {interaction.author} ({interaction.author.id})"   # Make sure to log this in case somebody adds some cringe.
        )

        return await interaction.send(f"Enjoy your shiny new emoji! {clonedEmoji}")
        

def setup(client):
    client.add_cog(
        ServerUtilities(
            client
        )
    )