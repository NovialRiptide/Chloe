import discord
from discord.ext import commands
from vars import *

class on_member_join_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.client.get_channel(JOIN_LEAVE_CHANNEL)
        embed=discord.Embed(
            color=0x0080ff,
            title=f"{member} has joined the server", 
            description=f"User ID: {member.id}"
        )
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(on_member_join_event(client))