import discord
from discord.ext import commands

from Classes.Setup_Video import Setup_Video

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
            q_text += [f'{index + 1}) [{item.title}]({item.url}) **[{item.requested_by}]**' for (index, item) in enumerate(q)]
            
            # Send queue
            return await self.nep.util.embed(c, '\n'.join(q_text))
        
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
        q = self.nep.util.get_queue(c.guild)._queue
        args = ' '.join(args).lower().split(' ')
        direct_play = False

        # Check for -d flag
        if args.index('-d') != -1:
            direct_play = True
        
        # Direct play without sending search results
        if direct_play == True:
            args.pop(args.index('-d'))

            r = self.nep.util.get_video('+'.join(args))
            # Handle fails
            if (r['state'] != 'success'):
                raise commands.CommandError(f'API error: {r["message"]}')
                return

            # Append video to queue
            video = Setup_Video(r['result'][0], c.author)
            q.append(video)

            q_embed = discord.Embed(
                description=f'📹 | Enqueued [{video.title}]({video.url}) **[{video.requested_by}]**',
                color=self.nep.util.r_color())
            q_embed.set_thumbnail(url=video.thumbnail)
            return await c.send(embed=q_embed)
        
        # Send search list
        r = self.nep.util.get_video('+'.join(args), 5)
        # Handle fail
        if (r['state'] != 'success'):
            raise commands.CommandError(f'API error: {r["message"]}')
            return
        
        input_str = ['Type **a number to chose** video (15 sec):']
        input_str += [f'{index + 1}) [{item.title}]({item.url})' for (index, item) in enumerate(r[''])]
        # Send inputs
        await self.nep.util.embed(c, '\n'.join(input_str))
        responses = await c.wait_for_message(author=c.message.author, timeout=15)

        await c.send(responses.clean_content)

    # ---------------------------------------------------

# Setup function
def setup(nep):
    nep.add_cog(Music(nep))
