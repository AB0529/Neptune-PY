import discord
from discord.ext import commands


# Info category
class Info(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = nep.get_cog('Utils')

    # Commands
    @commands.command(
        name='ping', 
        aliases=['pong'],
        description='Usual ping-pong command.'
        )
    async def ping(self, c):
        await c.send(embed=discord.Embed(
            title='🏓 Ping my pong', 
            description=f'⏱️ | **Message Delay**: `{self.nep.latency}`\n🔮 | **Shard**: `{self.nep.shard_id}`', 
            color=self.util.r_color))

def setup(nep):
    nep.add_cog(Info(nep))
