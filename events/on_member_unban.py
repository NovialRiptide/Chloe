import discord
from discord.ext import commands
from vars import *

class on_member_remove_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_unban(self, server, member):
        channel = self.client.get_channel(JOIN_LEAVE_CHANNEL)
        embed=discord.Embed(
            color=0x0080ff,
            title=f"{member} has been unbanned the server", 
            description=f"User ID: {member.id}"
        )
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(on_member_remove_event(client))