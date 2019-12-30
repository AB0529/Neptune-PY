import discord
from discord.ext import commands


# Info category
class Music(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = nep.get_cog('Utils')


    # Ping command
    @commands.command(
        name='queue', 
        aliases=['q'],
        description='Shows and manipulates the server\'s queue'
        )
    async def queue(self, c, *args):
        await c.send(args)

def setup(nep):
    nep.add_cog(Music(nep))
