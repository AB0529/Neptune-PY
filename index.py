# Imports
import asyncio
import os
import importlib

from dotenv import load_dotenv

# Import classes
Nep = importlib.import_module('Classes.Nep')

# Setup env variables
load_dotenv()
prefix = os.getenv('PREFIX')
token = os.getenv('TOKEN')

# Create config dict
config = {
    'prefix': prefix,
    'token': token
}

# Sets up bot
async def main():
    # Create bot
    nep = Nep.__init(config)
    
    # Login bot and logout on process end
    try:
        # Login
        await nep.start(token)
        # Load all cogs
        await nep.load_cogs()
    except KeyboardInterrupt:
        await nep.logout()

# Run main
asyncio.get_event_loop().run_until_complete(main())
