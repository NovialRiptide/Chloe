import json
import discord
from discord.ext import commands
from vars import *

class setup_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def setup(self, ctx):
        channel = ctx.message.channel
        template = {
            str(ctx.message.guild.id): {
                "auto_messages": {},
                "auto_announcer": True,
                "channels": {},
                "session_categories": {}
            }
        }
        with open("servers.json") as f:
            servers = json.load(f)
        try:
            with open("servers.json", "w") as json_file:
                json.dump(template, json_file)

            await channel.send("This server has been added to the Chloë database!")
        except KeyError:
            await channel.send("This server is already added to the Chloë database...")

def setup(bot):
    bot.add_cog(setup_cmd(bot))