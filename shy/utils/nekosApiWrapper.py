import aiohttp

class ShyNekosAPI(object):
    """
        A simple, personalized, SFW only python wrapper for nekos.api! 
    """

    NEKOS_BASEURL = "https://nekos.life/api/v2" # The base url to be used when making nekos.api requests

    @staticmethod
    def __prep_endpoint(endpoint) -> str:
        return ShyNekosAPI.NEKOS_BASEURL + "/" + endpoint

    @staticmethod
    async def __do_request(endpoint : str) -> str:
        async with aiohttp.ClientSession() as client_session:
            async with client_session.get(endpoint) as response:
                request = await response.json()

        return request["url"]

    @staticmethod
    async def pat() -> str:
        """Returns a random image representing patting.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/pat"
            )
        )

    @staticmethod
    async def hug() -> str:
        """Returns a random image representing hugging.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/hug"
            )
        )

    @staticmethod
    async def tickle() -> str:
        """Returns a random image representing tickling.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/tickle"
            )
        )

    @staticmethod
    async def poke() -> str:
        """Returns a random image representing poking.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/poke"
            )
        )

    @staticmethod
    async def feed() -> str:
        """Returns a random image representing feeding.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/feed"
            )
        )

    @staticmethod
    async def cuddle() -> str:                              # No idea if this is synonymous with "hugging"
        """Returns a random image representing cuddling.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/cuddle"
            )
        )

    @staticmethod
    async def kiss() -> str:
        """Returns a random image representing kissing.

        :return: The image url
        :rtype: str
        """
        return await ShyNekosAPI.__do_request(
            ShyNekosAPI.__prep_endpoint(
                "img/kiss"
            )
        )