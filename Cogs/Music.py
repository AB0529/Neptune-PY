import asyncio
import math

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
            q_text = [f':dancer: | **{len(q)}** total in the queue:\n']
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
        vc = c.guild.voice_client

        args = ' '.join(args).lower().split(' ')
        direct_play = True if '-d' in args else False
        
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
            q_embed.set_footer(text=f'Use {self.nep.config["prefix"]}play to play the queue!', icon_url=c.author.avatar_url)

            message = await c.send(embed=q_embed)
            return await self.check_vc(c, vc, message, q, video)
        
        # Send search list
        r = self.nep.util.get_video('+'.join(args), 5)
        # Handle fail
        if (r['state'] != 'success'):
            raise commands.CommandError(f'API error: {r["message"]}')
            return

        input_str = ['⏱️ | Type **a number to chose** a video (15 sec):\n']
        input_str += [f'{index + 1}) [{item["video"]["title"]}]({item["video"]["url"]})' for (index, item) in enumerate(r['result'])]
        # Get user input
        sent_list = await self.nep.util.embed(c, '\n'.join(input_str))

        try:
            responses = await self.nep.wait_for(
            'message', 
            check=lambda m: 
                # Check author
                m.author == c.message.author 
                # Make sure it's numeric
                and m.content.isdigit() 
                # Same size or les than results list
                and int(m.content) <= len(r['result']), 
            timeout=15)
        except asyncio.TimeoutError:
            return await sent_list.delete()

        # Push video to queue
        video = Setup_Video(r['result'][int(responses.clean_content) - 1], c.author)
        q.append(video)

        # Delete message
        await responses.delete()
        # Delete list
        await sent_list.delete()

        q_embed = discord.Embed(
            description=f'📹 | Enqueued [{video.title}]({video.url}) **[{video.requested_by}]**',
            color=self.nep.util.r_color())
        q_embed.set_thumbnail(url=video.thumbnail)
        q_embed.set_footer(text=f'Use {self.nep.config["prefix"]}play to play the queue!', icon_url=c.author.avatar_url)

        message = await c.send(embed=q_embed)
        await self.check_vc(c, vc, message, q, video)

    # ---------------------------------------------------
    
    # Checks vc status
    async def check_vc(self, c, vc, message, q, video):
        if vc and vc.channel:
            return
        
        if c.author.voice != None and c.author.voice.channel != None:
            channel = c.author.voice.channel
            client = await channel.connect()
            self.play_song(client, self.nep.util.get_queue(c.guild), video)
            message = await c.send('', embed=video.get_embed())

            return
        
        raise commands.CommandError('Need to be in a voice channel to do that.')
    
    # ---------------------------------------------------

    # Vote skip
    async def vote_skip(self, channel, member):
        q = self.nep.util.get_queue(channel.guild)
        q.skip_votes.add(member)

        users_in_channel = len([member for member in channel.members if not member.bot]) 

        if (float(len(q.skip_votes)) / users_in_channel) >= 0.5:
            channel.guild.voice_client.stop()
    # ---------------------------------------------------

    # Plays queue
    def play_song(self, client, q, video):
        q.now_playing = video
        q.skip_votes = set()
        source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(video.stream_url), volume=q.volume)


        def ap(err):
            if len(q._queue) > 0:
                q.next_song = q._queue.pop(0)
                self.play_song(client, q, video)
            else:
                asyncio.run_coroutine_threadsafe(client.disconnect(), self.nep.loop)
            
        client.play(source, after=ap)

    # ---------------------------------------------------


# Setup function
def setup(nep):
    nep.add_cog(Music(nep))
