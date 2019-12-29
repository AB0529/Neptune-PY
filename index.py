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

# Setup cogs
cogs_dir = 'Cogs'
cogs_list = os.listdir(cogs_dir)

# Load cogs
for cog in [f.replace('.py', '') for f in cogs_list if os.path.isfile(os.path.join(cogs_dir, f))]:
    try:
        nep.load_extension(cogs_dir + '.' + cog)
    except (discord.ClientException, ModuleNotFoundError):
        print(f'Failed to load cog {cog}')

# Login
nep.run(os.getenv('TOKEN'))
