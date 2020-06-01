import discord
from discord.ext import commands
from vars import *

class on_member_create_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_invite_create(self, invite):
        channel = self.client.get_channel(LOGGING_CHANNEL)
        embed=discord.Embed(
            color=0xff0000, 
            title=f"Invite Created: [{invite.inviter}]",
            description=f"Max Age: {invite.max_age} seconds\nUses: {invite.uses}\nMax Uses: {invite.max_uses}\nCode: {invite.code}"
        )
        await channel.send(embed=embed)

def setup(client):
    client.add_cog(on_member_create_event(client))