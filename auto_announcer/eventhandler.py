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

    @tasks.loop(seconds=1)
    async def auto_announcer(self):
        await self.client.wait_until_ready()
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            channel = self.client.get_channel(AUTO_ANNOUNCE_CHANNEL)
            last_msg = await channel.fetch_message(channel.last_message_id)
            if last_msg.author != self.client:
                msg = random.randint(0, len(servers[str(channel.guild.id)]["auto_messages"]))
                msg_id = list(servers[str(channel.guild.id)]["auto_messages"].keys())[msg]
                msg_data = servers[str(channel.guild.id)]["auto_messages"][msg_id]

                if servers[str(channel.guild.id)]["auto_announcer"]:
                    embed=discord.Embed(
                        title=msg_data["title"],
                        description=msg_data["desc"]
                    )
                    await channel.send(embed=embed)
        except:
            raise
            pass

def setup(client):
    client.add_cog(event_handler(client))