import discord, random
from discord.ext import commands


# Utils cog
class Utils(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.r_color = random.randint(0, 0xffffff)

    # Easy embed
    def embed(self, content):
        embed = discord.Embed(description=content, color=self.r_color)
        return embed

    # Easy error handle
    async def error(self, c, _type, error='Error handler errored, wack'):
        await c.send(embed=self.embed(f':x: Error | Oh nose, an **error occured**!\n```css\nType: {_type}\nError: {error}\n```'))

def setup(nep):
    nep.add_cog(Utils(nep))
