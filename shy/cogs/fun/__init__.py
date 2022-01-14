from cogs.fun.funcogs.reactions import ReactionCommands

def setup(client):
    ReactionCommands.load_cog_into_client(client)
