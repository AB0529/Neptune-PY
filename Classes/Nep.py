import os

import discord
from discord.ext import commands
from termcolor import colored

import asyncio
from Classes.Utils import Utils


# Custom bot class extending commands.Bot
class Nep(commands.Bot):
    def __init__(self, config: dict):
        self.config = config

        super().__init__(
            config=self.config,
            command_prefix=self.config['prefix'],
            ownerIds=[184157133187710977, 251091302303662080],
            case_insensitive=True,
            description='Python rewrite of Neptune'
        )

        self.util = Utils(self)
    
    # ---------------------------------------------------
    
    # Loads all cogs from Cogs folder
    async def load_all_extensions(self):
        # Get cogs
        cogs = self.util.get_all_cogs()

        # Attempt to load cogs
        for cog in cogs:
            try:
                self.load_extension(f'Cogs.{cog}')
                self.util.log('Cogs', f'Cog loaded', os.path.basename(cog))
            except Exception as e:
                self.util.log('Cogs', f'Error loading cog {colored(os.path.basename(cog), "magenta")} !', 'ERROR')

    # ---------------------------------------------------
    
    # Reloads all cogs 
    async def reload_all_extensions(self):
        # Get cogs
        cogs = self.util.get_all_cogs()

        # Attempt reload
        for cog in cogs:
            try:
                self.reload_extension(f'Cogs.{cog}')
            except Exception as e:
                self.util.log('Cogs', f'Error reloading cog {colored(os.path.basename(cog), "magenta")} !', 'ERROR')

    # ---------------------------------------------------

    # Handle on_ready event
    async def on_ready(self):
        self.util.log('Ready', f'Bot logged in as {colored(f"{self.user.name}#{self.user.discriminator}", "green")}')

        # Load cogs
        await self.load_all_extensions()

    # ---------------------------------------------------

    # Handles on_message event
    async def on_message(self, msg):
        # Ignore bots
        if msg.author.bot:
            return

        # Process command
        await self.process_commands(msg)

    # ---------------------------------------------------
