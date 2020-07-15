import discord
import random
import asyncio
from discord.ext import commands
from vars import *

class on_member_join_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await asyncio.sleep(5)
        try:
            random_role = random.randint(0,len(HOUSE_ROLES)-1)
            guild = member.guild
            role = guild.get_role(HOUSE_ROLES[random_role])
            
            await member.add_roles(role)
            
            channel = self.client.get_channel(JOIN_MSG_CHANNEL)

            join_msg = PUBLIC_WELCOMER_MSG
            join_msg = join_msg.replace("{mention}", member.mention)
            await channel.send(join_msg)
            
            await member.send(PRIVATE_WELCOMER_MSG)
        except: pass

def setup(client):
    client.add_cog(on_member_join_event(client))