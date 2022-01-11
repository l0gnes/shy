import disnake
from disnake.ext import commands

from pydoc import locate
import inspect
from textwrap import dedent
import re

class DevelopmentUtilities(commands.Cog, name="Development"):

    FUNCTION_CALL_STRIPPER = re.compile(r"(?<=[0-9a-zA-Z._])(\(.*\))")
    URL_FILTER = re.compile(r"http[|s]:\/\/[a-zA-Z0-9_.\/-]*")

    def __init__(self, client : disnake.Client):
        self.client = client

    @commands.slash_command(
        name = "pydoc",
        description = "Grabs a docstring from python modules",
    )
    async def developmentPydocCommands(
        self, 
        interaction : disnake.ApplicationCommandInteraction, 
        term : str
    ):
        term = self.FUNCTION_CALL_STRIPPER.sub(
            "",
            term,
        )

        convertedInstance = locate(term)

        if convertedInstance is None:
            return await interaction.send(
                f"Failed to locate the term: `{term}`."
            )

        if hasattr(convertedInstance, "__doc__"):

            try:
                term_signature = inspect.signature(
                    convertedInstance
                )
            except ValueError:

                # TODO(Alexander): Find a way to fix this gross nested try-except

                if hasattr(convertedInstance, "__call__"):
                    try:
                        term_signature = inspect.signature(
                            convertedInstance.__call__
                        )
                    except ValueError:

                        term_signature = "(?)"


            term_docs = inspect.getdoc(convertedInstance)

            if hasattr(convertedInstance, "__module__"):
                thingName = convertedInstance.__module__ + "." + convertedInstance.__qualname__ if convertedInstance.__module__ != "builtins" else convertedInstance.__qualname__
            else:
                thingName = convertedInstance.__qualname__
    
            methods = [
                m for m in inspect.getmembers(convertedInstance)
                if not m[0].startswith("__")
            ]

            return await interaction.send(
                embed = disnake.Embed(
                    colour = 0xEAEAEA,
                    description = dedent(
                        f"""
                        ```py
{convertedInstance.__qualname__}{term_signature if hasattr(convertedInstance, '__call__') else ''}```
                        {term_docs}
                        """
                    ),
                ).set_author(
                    name = thingName + ('()' if hasattr(convertedInstance, "__call__") else ''),
                    icon_url = interaction.author.avatar
                ).set_footer(
                    text = f"📝 There are {len(methods)} methods for this type." if methods else disnake.embeds.EmptyEmbed
                )
            )

    @commands.slash_command(
        name = "fetchone",
        description = "Grabs a single record from an api response"
    )
    async def apiFetchoneResponse(self, interaction : disnake.ApplicationCommandInteraction, url : str):
        raise NotImplementedError
    

        
def setup(client):
    client.add_cog(
        DevelopmentUtilities(
            client
        )
    )
        
