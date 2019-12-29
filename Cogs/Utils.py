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


def setup(nep):
    nep.add_cog(Utils(nep))
