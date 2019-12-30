from discord.ext import commands

# Owner category
class Owner(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = nep.get_cog('Utils')

    # Kill command
    @commands.command(
        name='kill',
        aliases=['stop'],
        hidden=True,
        description='Logs bot out and kills process'
        )
    @commands.is_owner()
    async def kill(self, c):
        await c.send('Killing...')
        await self.nep.logout()
    # Set status command
    @commands.command(
        name='status',
        aliases=['ss'],
        hidden=True,
        description='Logs bot out and kills process'
        )
    @commands.is_owner()
    async def status(self, c, _type='playing', *status):
        status = ' '.join(status)
        acceptable_tpyes = ['playing', 'watching', 'listening']

        if _type not in acceptable_tpyes:
            return await self.util.error(c, 'Invalid Args', f'`{_type}` is not an acceptable type!')
        
        await c.send(f'Type: {_type}\nStatus: {" ".join(status)}')

def setup(nep):
    nep.add_cog(Owner(nep))