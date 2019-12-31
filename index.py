# Imports
import asyncio
import os

from Classes.Nep import Nep
from dotenv import load_dotenv

# Setup env variables
load_dotenv()
prefix = os.getenv('PREFIX')
token = os.getenv('TOKEN')
api_key = os.getenv('API_KEY')
api_url = os.getenv('API_URL')

# Create config dict
config = {
    'prefix': prefix,
    'token': token,
    'api_key': api_key,
    'api_url': api_url
}

# Sets up bot
async def main():
    # Create bot
    nep = Nep(config)

    # Login bot and logout on process end
    try:


        # Login
        await nep.start(token)


    except KeyboardInterrupt:
        await nep.logout()

# Run main
asyncio.get_event_loop().run_until_complete(main())
