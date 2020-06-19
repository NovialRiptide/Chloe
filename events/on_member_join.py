import discord
import json
from discord.ext import commands
from vars import *

class on_member_join_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_member_join(self, member):    
        with open("servers.json") as f:
            servers = json.load(f)
        server = servers[str(member.guild.id)]
        channel = self.client.get_channel(server["channels"]["join_leave"])
        try:
            if server["join_msg"] != "":
                join_msg = server["join_msg"]
                join_msg = join_msg.replace("{mention}", member.mention)
                await channel.send(join_msg)
        except:
            pass
        
        try:
            if server["join_msg_dm"] != "":
                await member.send(server["join_msg_dm"])
        except:
            pass

def setup(client):
    client.add_cog(on_member_join_event(client))