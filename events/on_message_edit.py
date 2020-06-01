import discord
from discord.ext import commands
from vars import *

class on_message_edit_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        channel = self.client.get_channel(LOGGING_CHANNEL)
        embed=discord.Embed(
            color=0xff0000, 
            title=f"Message Edited: [{before.author}] in #{before.channel}",
            description=f"Before: {before.content}\nAfter: {after.content}"
        )
        if before.author != self.client.user:
            await channel.send(embed=embed)
            
def setup(client):
    client.add_cog(on_message_edit_event(client))