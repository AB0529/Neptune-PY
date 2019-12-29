from discord.ext import commands


# Events cog
class Events(commands.Cog):
    def __init__(self, nep):
        self.nep = nep

    # Ready event
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Client logged in as {self.nep.user.name}')


def setup(nep):
    nep.add_cog(Events(nep))
