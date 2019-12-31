import random

import discord
from termcolor import colored


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

    # Easier embeds
    async def embed(self, c, content):
        embed = discord.Embed(description=content, color=self.r_color())

        await c.send(embed=embed)

    # ---------------------------------------------------

    # Handle errors 
    async def error(self, c, title, error):
        await self.embed(c, f':x: Error | Oh fucking shit, an **error occured**!\n```xl\nType: {title}\n\n{error}\n```')

    # ---------------------------------------------------
