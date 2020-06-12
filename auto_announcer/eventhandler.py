import discord
from discord.ext import commands, tasks
import json
import random
from vars import *

class event_handler(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.auto_announcer.start()

    def unload(self):
        self.auto_announcer.cancel()

    @tasks.loop(hours=1)
    async def auto_announcer(self):
        await self.client.wait_until_ready()
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            
            server_ids = list(servers)
            for server in range(len(servers)):
                channel = self.client.get_channel(servers[str(server_ids[server])]["channels"]["auto_announce"])
                channel_history = await channel.history(limit=1).flatten()
                number_of_auto_msgs = len(list(servers[str(server_ids[server])]["auto_messages"]))

                if number_of_auto_msgs > 0:
                    msg = random.randint(0, len(servers[str(channel.guild.id)]["auto_messages"])-1)
                    msg_id = list(servers[str(channel.guild.id)]["auto_messages"].keys())[msg]
                    msg_data = servers[str(channel.guild.id)]["auto_messages"][msg_id]

                    embed=discord.Embed(
                        title=msg_data["title"],
                        description=msg_data["desc"]
                    )
                    if channel_history[0].author.id != self.client.user.id:
                        await channel.send(embed=embed)
        except:
            raise
            pass

def setup(client):
    client.add_cog(event_handler(client))