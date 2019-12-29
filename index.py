# Import libs
import os

from discord.ext import commands
from dotenv import load_dotenv

# Setup .env
load_dotenv()

# Initalize the bot
nep = commands.Bot(
    description='A Python rewrite of Neptune.',
    command_prefix=os.getenv('PREFIX'),
    ownerIds=[184157133187710977, 251091302303662080],
    )



# Login
nep.login(os.getenv('TOKEN'))
