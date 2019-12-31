import os

import discord
from discord.ext import commands
from termcolor import colored

import Utils


# Custom bot class extending commands.Bot
class Nep(commands.Bot):
    def __init__(self, config):
        self.config = config
        self.utils = Utils(self)

        super().__init__(
            config=self.config,
            command_prefix=self.config['prefix'],
            ownerIds=[184157133187710977, 251091302303662080],
            case_insensitive=True,
            description='Python rewrite of Neptune'
        )
    
    # ---------------------------------------------------
    
    # Loads all cogs from Cogs folder
    async def load_all_extensions(self):
        await self.wait_until_ready()
        
        # Get cogs
        cogs = [f.replace('.py', '') for f in os.listdir('Cogs') if not f.startswith('__')]
        # Attempt to load cogs
        for cog in cogs:
            try:
                self.load_extension(f'Cogs.{cog}')
                self.utils.log('Cogs', f'Cog {colored(os.path.basename(cog), "magenta")} loaded')
            except Exception as e:
                self.utils.log('Cogs', f'Error loading cog {colored(os.path.basename(cog), "magenta")} !', 'ERROR')

    # ---------------------------------------------------
