# Import libs
import sys
import os

import discord
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

# Load cogs from cogs dir
[nep.load_extension(f'Cogs.{f.replace(".py", "")}') for f in os.listdir('Cogs') if not f.startswith('__')]

# Login
nep.run(os.getenv('TOKEN'))
