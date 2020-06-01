import discord
from discord.ext import commands
from vars import *

class on_message_delete_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel = self.client.get_channel(LOGGING_CHANNEL)
        embed=discord.Embed(
            color=0xff0000, 
            title=f"Message Deleted: [{message.author}] in #{message.channel}",
            description=f"Contents: {message.content}"
        )
        await channel.send(embed=embed)
            
def setup(client):
    client.add_cog(on_message_delete_event(client))