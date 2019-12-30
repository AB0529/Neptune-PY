import discord, os, requests
from discord.ext import commands


# Info category
class Info(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
        self.util = nep.get_cog('Utils')


    # Ping command
    @commands.command(
        name='ping', 
        aliases=['pong'],
        description='Usual ping-pong command.'
        )
    async def ping(self, c):
        await c.send(embed=discord.Embed(
            title='🏓 Ping my pong', 
            description=f'⏱️ | **Message Delay**: `{round(self.nep.latency, 2)}sec`\n🔮 | **Shard**: `{self.nep.shard_id}`', 
            color=self.util.r_color))
    # Help command
    @commands.command(
        name='help',
        aliases=['h'],
        description='Shows this message.'
    )
    async def help(self, c, arg=None):
        first_embed = discord.Embed(color=self.util.r_color)

        # Set category field
        categories = [f'**{f.replace(".py", "")}**'for f in os.listdir('Cogs') if not f.startswith('__')]
        first_embed.add_field(name='📜 Categories', value='\n'.join(categories))

        # Set Misc. field
        misc = [f'- [Nep Church](https://discord.gg/HU5ZanK)']
        first_embed.add_field(name='🤷‍♀️ Misc', value='\n'.join(misc), inline=False)

        # Set footer field
        first_embed.set_footer(text=f'{os.getenv("PREFIX")}help <COMMAND or CATEGORY>', icon_url=c.message.author.avatar_url)

        # Send first help embed
        await c.send(embed=first_embed)

        # Handle args
        print(self)

def setup(nep):
    nep.add_cog(Info(nep))
