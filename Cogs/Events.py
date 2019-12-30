from discord.ext import commands


# Events cog
class Events(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = nep.get_cog('Utils')

    # Ready event
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Client logged in as {self.nep.user.name}')

    # On command error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        await self.util.error(ctx, 'Command Error', str(exc))

def setup(nep):
    nep.add_cog(Events(nep))
