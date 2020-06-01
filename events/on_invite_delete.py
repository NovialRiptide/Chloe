import discord
from discord.ext import commands
from vars import *

class on_invite_delete_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_invite_delete(invite):
        channel = self.client.get_channel(LOGGING_CHANNEL)
        embed=discord.Embed(
            color=0xff0000, 
            title=f"Invite Deleted: [N/A]",
            description=f"Code: {invite.code}"
        )
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(on_invite_delete_event(client))