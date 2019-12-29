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

# Ready event
@nep.event
async def on_ready():
    print(f'Client logged in as {nep.user.name}')

# TODO: setup cogs
# Test command
@nep.command(name='ping', description='Usual ping-pong command.')
async def ping(c):
    await c.send('Pongy pong pong')

@nep.command(name='kill', description='Logs bot out and kills process')
async def kill(c):
    if await nep.is_owner(c.message.author) == False:
        await c.send('Not owner.')
        return
    
    await c.send('Killing...')
    await nep.logout()

# Login
nep.run(os.getenv('TOKEN'))
