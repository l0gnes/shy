from typing import Coroutine, List
from disnake import ApplicationCommandInteraction
from glob import glob
from os.path import split

async def quickDefer(interaction : ApplicationCommandInteraction) -> Coroutine:
    """
    Quickly defers the interaction, allowing it to be done within code
    on one line instead of the two required lines by default

    :param interaction: The interaction to defer
    :type interaction: ApplicationCommandInteraction
    :return: The deferred message?
    :rtype: Coroutine
    """
    return await interaction.response.defer()
    
def fetchAllAvailableCogs() -> List[str]:
    """Returns all of the cog names for cogs in the ./cogs/ dir

    :return: A list of unprefixed cog names
    :rtype: List[str]
    """
    allCogFiles = glob("./**/cogs/**.py")
    return [split(path)[1][:-3] for path in allCogFiles]
    