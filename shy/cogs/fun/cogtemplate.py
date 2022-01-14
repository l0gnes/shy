from disnake.ext import commands

class Cog(commands.Cog):

    @classmethod
    def load_cog_into_client(cls, client):
        client.add_cog(
            cls(
                client = client
            )
        )