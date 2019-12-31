import discord
from discord.ext import commands

# Create events cog
class Music(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    @nep.group()
    async def show(self, c):
        await c.sed('Su')
    # Queue command
    @commands.command(
        name='queue', 
        aliases=['q'],
        description='Modify and show the server\'s queue.')
    async def queue(self, c, *, flags):
        await c.send(flags)

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Music(nep))
