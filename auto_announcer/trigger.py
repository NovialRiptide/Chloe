import discord
import json
from discord.ext import commands
from vars import *

class trigger_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["aa"])
    async def announcer(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(MISSING_ARGUMENTS_ERROR)

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def enable(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            servers[str(ctx.message.guild.id)]["auto_announcer"] = True

            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
            await ctx.send("Auto Announcer has been enabled!")
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def disable(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            servers[str(ctx.message.guild.id)]["auto_announcer"] = False
                
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
            await ctx.send("Auto Announcer has been disabled!")
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(trigger_cmd(bot))