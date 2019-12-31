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
    async def queue(self, c, *, args):
        # List of acceptable flags
        acceptable_flags = {
            'list': ['sq', 'li', 'show'],
            'remove': ['rm']
        }
        correct_flag = self.util.get_queue_flags(args, acceptable_flags)
        # Check for correct flags
        if correct_flag == None:
            return self.util.error(c, 'Unvalid arguments', f'Acceptable flags are: {acceptable_flags}')

        await c.send(f'{args}\n{correct_flag}')

def setup(nep):
    nep.add_cog(Music(nep))
