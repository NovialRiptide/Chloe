import json
import discord
from discord.ext import commands
from vars import *

class welcomer(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def join_msg_dm(self, ctx, *, message: str):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            servers[str(ctx.guild.id)]["join_msg_dm"] = message
            await ctx.channel.send("Added join direct message!")
            
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(welcomer(bot))