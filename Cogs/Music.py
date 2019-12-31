import discord
from discord.ext import commands

# Create events cog
class Music(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    # Queue command
    @commands.command(
    name='queue',
    aliases=['q'],
    descrription='Shows the queue')
    async def queue(self, c):
        pass

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Music(nep))
