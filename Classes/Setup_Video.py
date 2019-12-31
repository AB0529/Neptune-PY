import discord

# Creates the video object
class Setup_Video:
    def __init__(self, v, requestor):
        self.stream_url = v['video']['url'] # Stream url
        self.url = v['video']['url'] # Video url
        self.title = v['video']['title'] # Video title
        self.thumbnail = v['thumbnail']['default']['url'] # Video thumbnail url
        self.requested_by = requestor # Song requestor
    
    # ---------------------------------------------------

    # Create embed from video info
    def get_embed(self):
        embed = discord.Embed(description=f'🎥 | [{self.title}]({self.url}) **[{self.requested_by}]**')
        embed.set_thumbnail(url=self.thumbnail)

        return embed

    # ---------------------------------------------------