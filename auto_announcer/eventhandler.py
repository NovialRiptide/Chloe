import discord
from discord.ext import commands, tasks
import json
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
            channel = self.client.get_channel(AUTO_ANNOUNCE_CHANNEL)
            if servers[str(channel.guild.id)]["auto_announcer"]:
                await channel.send("WEEEEE")
        except:
            pass

def setup(client):
    client.add_cog(event_handler(client))