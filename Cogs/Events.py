import discord
from discord.ext import commands

# Create events cog
class Events(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    # Handles errors on commands
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        # Ignore command not existing
        if isinstance(exc, commands.CommandNotFound):
            return

        self.nep.util.log(f'Command Error', exc, f'{ctx.author.name}#{ctx.author.discriminator}')
        await self.util.error(ctx, 'Command Error', exc)

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Events(nep))