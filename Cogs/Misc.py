import discord
from discord.ext import commands

# Create events cog
class Misc(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    # Ping command
    @commands.command(
        name='ping', 
        aliases=['pong'],
        description='Usual ping-pong command.')
    async def ping(self, c):
        await c.send(embed=discord.Embed(
            title='🏓 Ping my pong', 
            description=f'⏱️ | **Message Delay**: `{round(self.nep.latency, 2)}sec`\n🔮 | **Shard**: `{self.nep.shard_id}`', 
            color=self.nep.util.r_color()))

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Misc(nep))