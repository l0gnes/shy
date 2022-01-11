from core.client import shyDiscordBot
import dotenv, os, argparse

parser = argparse.ArgumentParser(
    description = "shy Discord Bot CLI interface"
)
parser.add_argument('-d', help="Sets the bot to run in debugging mode", action='store_true')
parser.add_argument('-v', help="Sets the bot to run with verbose file logging", action='store_true')

if __name__ == "__main__":
    dotenv.load_dotenv()
    args = parser.parse_args()

    shyDiscordBot.startShy(
        os.environ.get("TOKEN"),
        verbose = args.v,
        debug = args.d
    )