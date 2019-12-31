import discord
from discord.ext import commands

# Create events cog
class Music(commands.Cog):
    def __init__(self, nep):
        self.nep = nep
    
    # ---------------------------------------------------

    # Queue command
    @commands.command(
    name='queue',
    aliases=['q'],
    descrription='Shows the queue')
    @commands.guild_only()
    async def queue(self, c):
        q = self.nep.util.get_queue(c.guild)._queue

        # Find queue text
        if len(q) > 0:
            q_text = [f':dancer: | **{len(q)}** total in the queue:']
            q_text += [
                f'{index + 1}) [{item.title}]({item.link}) **[{item.requested_by}]**' for (index, item) in enumerate(q)]
            
            # Send queue
            return await self.nep.util.embed(c, q_text.join('\n'))
        
        # Queue is empty
        await self.nep.util.embed(c, '<a:WhereTf:539164678480199720> | *You can\'t list anything if there\'s nothing to list*')
        

    # ---------------------------------------------------

    # Plays music from url or search string
    @commands.command(
        name='play',
        aliases=['p'],
        description='Plays song from url or keyword(s)'
    )
    @commands.guild_only()
    async def play(self, c, *args):
        args = ' '.join(args).lower().split(' ')
        direct_play = False

        # Check for -d flag
        if args.index('-d') != -1:
            direct_play = True
        
        # Direct play without sending search results
        if direct_play == True:
            args = args.pop('-d')

            result = self.nep.util.get_video(' '.join(args))
            await c.send(result)

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Music(nep))
