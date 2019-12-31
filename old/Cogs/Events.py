from discord.ext import commands


# Events cog
class Events(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = self.nep.get_cog('Utils')

    # -----------------------------------------------------------------

    # On command error
    @commands.Cog.listener()
    async def on_command_error(self, ctx, exc):
        # Ignore command not existing
        if isinstance(exc, commands.CommandNotFound):
            return

        print(f'[{ctx.author.name}#{ctx.author.discriminator}] - {ctx.author.guild.id} - {ctx.author.guild.name}] <> {exc}')
        await self.util.error(ctx, 'Command Error', exc)

    # -----------------------------------------------------------------

def setup(nep):
    nep.add_cog(Events(nep))
