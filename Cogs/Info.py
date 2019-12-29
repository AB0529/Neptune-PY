from discord.ext import commands


# Info category
class Info(commands.Cog):
    def __init__(self, nep):
        self.nep = nep

    # Commands
    @commands.command(
        name='ping', 
        aliases=['pong'],
        description='Usual ping-pong command.'
        )
    async def ping(self, c):
        await c.send('Pingy pong pong')

def setup(nep):
    nep.add_cog(Info(nep))
