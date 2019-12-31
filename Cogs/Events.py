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
        # Respond to command disabled for dm
        elif isinstance(exc, commands.NoPrivateMessage):
            return await self.util.embed(ctx, f':x: | `{ctx.command}` cannot be used in DMs!')

        self.nep.util.log(f'Command Error', exc, f'{ctx.author.name}#{ctx.author.discriminator}')
        await self.nep.util.error(ctx, 'Command Error', exc.__cause__)

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Events(nep))