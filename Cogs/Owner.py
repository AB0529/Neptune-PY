import discord
from discord.ext import commands

# Create events cog
class Owner(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    # Set status command
    @commands.command(
        name='status',
        aliases=['ss'],
        hidden=True,
        description='Changes bot activity')
    @commands.is_owner()
    async def status(self, c, _type='playing', *status):
        status = ' '.join(status)
        acceptable_tpyes = ['playing', 'watching', 'listening']

        # Make sure correct type is used
        if _type not in acceptable_tpyes:
            return await self.nep.util.error(c, 'Invalid Args', f'`{_type}` is not an acceptable type!')
        
        # Set the activity
        await self.nep.change_presence(activity=discord.Activity(name=status, type=discord.ActivityType[_type.lower()]))
        await self.nep.util.embed(c, f'✅ | Activity changed to `{_type.upper()} {status}`')

    # ---------------------------------------------------

    # Reloads a cog
    @commands.command(
        name='reload',
        aliases=['re'],
        hidden=True,
        descrription='Reloads a specified cog')
    @commands.is_owner()
    async def reload(self, c, cog):
        cogs = self.nep.util.get_all_cogs()

        # Reloads all cogs
        if cog.lower() == 'all':
            await self.util.embed(c, f'🌀 | Cogs `{", ".join(cogs)}` have been reloaded')
            self.nep.load_all_cogs()

        # Reload cog
        self.nep.reload_extension(f'Cogs.{cog.capitalize()}')
        await self.util.embed(c, f'🌀 | Cog `{cog}` has been reloaded')

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Owner(nep))