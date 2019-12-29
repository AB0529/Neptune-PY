from discord.ext import commands

# Owner category
class Owner(commands.Cog):
    def __init__(self, nep):
        self.nep = nep

    # Commands
    @commands.command(name='kill', description='Logs bot out and kills process')
    @commands.is_owner()
    async def kill(self, c):
        if await self.nep.is_owner(c.message.author) == False:
            await c.send('Not owner.')
            return
        
        await c.send('Killing...')
        await self.nep.logout()

def setup(nep):
    nep.add_cog(Owner(nep))