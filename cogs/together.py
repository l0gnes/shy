import json
from enum import Enum
import disnake
from disnake.ext import commands
import aiohttp

togetherIds = {
    "Watch Together": "880218394199220334", 
    #"youtubedev": "880218832743055411", 
    "Poker Night": "755827207812677713",
    "Betrayal.io": "773336526917861400",
    "Fishington.io": "814288819477020702",
    "Chess in the Park": "832012774040141894",
    #"chessdev": "832012586023256104", 
    "Letter Tile": "879863686565621790", 
    "Word Snacks": "879863976006127627", 
    "Doodle Crew": "878067389634314250", 
    "Awkword": "879863881349087252", 
    "SpellCast": "852509694341283871",
    "Checkers In The Park": "832013003968348200",
    "PuttParty": "763133495793942528", 
    "SketchyArtist": "879864070101172255" 
}

class Together(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.slash_command(
        name = "together",
        description="Start a Discord Together game",
    )
    @commands.guild_only()                              # This can only be used in guilds (duh)
    async def _discordTogether(
        self,
        inter,
        game = commands.Param(choices=togetherIds),
        channel : disnake.VoiceChannel = commands.Param()
    ):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"https://discord.com/api/v8/channels/{channel.id}/invites",
                data = json.dumps(dict(
                    max_age = 86400,
                    max_uses = 0,
                    target_application_id = game,
                    target_type = 2,
                    temporary = False,
                    validate = None
                )),
                headers = {
                    "Authorization" : f"Bot {self.client.http.token}",
                    'Content-Type' : "application/json"
                }
            ) as resp:
                r = await resp.json()

            gameName = list(togetherIds.keys())[list(togetherIds.values()).index(game)]
            
            return await inter.send(
                embed = disnake.Embed(
                    colour = 0xeaeaea
                ).set_author(
                    name = f"Click here to play {gameName}",
                    icon_url = inter.user.avatar,
                    url= f"https://discord.gg/{r['code']}"
                ),
                ephemeral = True
            )

def setup(client):
    client.add_cog(
        Together(client)
    )