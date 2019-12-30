import discord, random
from discord.ext import commands


# Utils cog
class Utils(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.r_color = random.randint(0, 0xffffff)

    # -----------------------------------------------------------------

    # Easy embed
    async def embed(self, c, content):
        embed = discord.Embed(description=content, color=self.r_color)
        await c.send(embed=embed)

    # -----------------------------------------------------------------

    # Easy error handle
    async def error(self, c, _type='Idfk', error='Error handler errored, wack'):
        await self.embed(c, f':x: Error | Oh nose, an **error occured**!\n```css\nType: {_type}\n\n{error}\n```')

    # -----------------------------------------------------------------

def setup(nep):
    nep.add_cog(Utils(nep))
