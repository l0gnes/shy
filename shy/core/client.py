from disnake import Intents, Activity
import disnake
from disnake.enums import ActivityType
from disnake.ext import commands
from datetime import datetime
from textwrap import dedent
#from .database import DatabaseHandler

class shyDiscordBot(commands.AutoShardedInteractionBot):

    VERBOSE_LOGGING = False
    DEBUG_MODE = False
    AUTOLOAD_COGS = (
        "cogs.together",
        "cogs.info",
        "cogs.development",
        "cogs.serverutils"
    )

    COMMANDS_EXECUTED = 0

    def __init__(self, *args, **kwargs):

        super().__init__(
            #command_prefix=".",
            intents = Intents.all(),
            activity = Activity(
                name = "ˏˋ°•*⁀➷",
                type = ActivityType.watching,
            ),
            test_guilds=[
                917316133714010132
            ],
            *args, **kwargs
        )

        self.add_listener(self.shyStartupMessage, name="on_ready")
        self.add_listener(self.commandCounting, name="on_slash_command")

        # TODO(boopdev): Implement Prisma instead 
        #self.db = self.loop.run_until_complete(DatabaseHandler.init_database())

        self.loadStartupCogs()

        self.BOT_INVITE_URL = disnake.utils.oauth_url(
            client_id = 926293083136622692,                     # NOTE: I hate this
            permissions = disnake.Permissions.all_channel(),    # TODO: Actually figure out what the bot only needs and stop using this
            scopes = [
                "bot",
                "applications.commands"
            ]
        )

    async def get_context(self, message, *, cls=None):
        return await super().get_context(message, cls=cls or ShyContext)

    def loadStartupCogs(self):
        for ext in self.AUTOLOAD_COGS:
            try:
                self.load_extension(ext)
            except Exception as err:
                print(err)
            else:
                print(f"{ext} was loaded")

    @classmethod
    def startShy(cls, token : str, *args, **kwargs) -> None:
        new = cls()
        
        # Setting up constants for this bot session
        new.VERBOSE_LOGGING = kwargs.get('verbose', False)
        new.DEBUG = kwargs.get('debug', False)
        
        new.run(
            token
        )

    async def shyStartupMessage(self):
        appInfo = await self.application_info()
        botUser = self.user
        guildCount = len(self.guilds)
        commandCount = len(self.slash_commands)
        cogCount = len(self.cogs)
        startedTime = datetime.now().strftime("%x %I:%M:%S %p")
        print(
            dedent(
                f"""
                {botUser} || {botUser.id}
                ------------------------------
                Guild Count: {guildCount:,}
                Command Count: {commandCount:,}
                Cog Count: {cogCount:,}
                Started Time: {startedTime}
                """
            )
        )

    async def commandCounting(self, cmd):
        self.COMMANDS_EXECUTED += 1