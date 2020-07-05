import discord
import random
import json
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
            
            with open("servers.json") as f:
                servers = json.load(f)
            server = servers[str(member.guild.id)]
            channel = self.client.get_channel(server["channels"]["join_leave"])
            try:
                if server["join_msg"] != "":
                    join_msg = server["join_msg"]
                    join_msg = join_msg.replace("{mention}", member.mention)
                    await channel.send(join_msg)
            except: pass
            
            try:
                if server["join_msg_dm"] != "":
                    await member.send(server["join_msg_dm"])
            except: pass
        except: pass

def setup(client):
    client.add_cog(on_member_join_event(client))