import os
import random
import requests

import discord
from discord.ext import commands
from termcolor import colored

from Classes.Setup_Queue import Setup_Queue

# Utils class
class Utils:
    def __init__(self, nep):
        self.nep = nep

    # ---------------------------------------------------
    
    # Creates random hex color
    def r_color(self):
        return random.randint(0, 0xffffff)

    # ---------------------------------------------------

    # Prettier log
    def log(self, title='no title', content='no content', misc=''):
        print(f'[{colored(title, "blue")}] <> {content} ({colored(misc, "yellow")})')


    # ---------------------------------------------------

    # Retrive list of all cogs
    def get_all_cogs(self):
        cogs = [f.replace('.py', '') for f in os.listdir('Cogs') if not f.startswith('__')]

        return cogs

    # ---------------------------------------------------

    # Easier embeds
    async def embed(self, c, content):
        embed = discord.Embed(description=content, color=self.r_color())

        await c.send(embed=embed)

    # ---------------------------------------------------

    # Seaches Nep API for YouTube video
    def get_video(self, search, max_resulsts=1):
        r = requests.get(f'{self.nep.config["api_url"]}/yt_video?key={self.nep.config["api_key"]}&search={search}&max_results={max_resulsts}')

        return r.json()

    # ---------------------------------------------------

    # Handle errors 
    async def error(self, c, title, error):
        await self.embed(c, f':x: Error | Oh fucking shit, an **error occured**!\n```xl\nType: {title}\n\n{error}\n```')



    # =-=-=-=-=-=-==-=-=-=-=-=-==-=-=-=-=-=-==-=-=-=-=-=-
    # Music
    # =-=-=-=-=-=-==-=-=-=-=-=-==-=-=-=-=-=-==-=-=-=-=-=-


    # Returns the queue for the guild
    # TODO: Move this into MongoDB/SQLite
    def get_queue(self, guild):
        # Check if guild id is in queues
        if guild.id in self.nep.queues:
            return self.nep.queues[guild.id]
        
        # If not, add it and return the queue
        self.nep.queues[guild.id] = Setup_Queue()
        print(self.nep.queues)
        return self.nep.queues[guild.id]

    # ---------------------------------------------------

    # Checks if bot is currently playing
    async def is_playing(self, c):
        voice_client = c.guild.voice_client

        # Is playing
        if voice_client and voice_client.channel and voice_client.source:
            return True
        
        # Not playing, raise not playing error
        raise commands.Command('Not currently playing anything.')

    # ---------------------------------------------------

    # Checks if author is in same voice channel as bot
    async def is_in_voice_channel(self, c):
        voice = c.author.voice
        nep_voice = c.guild.voice_client

        # Is in voice channel
        if voice and nep_voice and voice.channel and nep_voice.channel and voice.channel == nep_voice.channel:
            return True
        
        # If not, raise not in same vc error
        raise commands.CommandError('Not in the same channel as bot to do this.')

    # ---------------------------------------------------

    # Checks if the author is the audio reqestor
    async def is_audio_requestor(self, c):
        queue = await self.get_queue(c.guild)
        perms = c.channel.permissions_for(c.author)

        # Check if user is admin or requestor
        if perms.adimistrator or queue.is_requestor(c.author):
            return True
        
        # If not requestor, raise error
        raise commands.CommandError('Need to be the song requestor to do that.')

    # ---------------------------------------------------
    
