import discord
import json
import random
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

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def add_msg(self, ctx, *, title: str):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            msg_id = random.randint(1,100000)

            servers[str(ctx.message.guild.id)]["auto_messages"][str(msg_id)] = {}
            servers[str(ctx.message.guild.id)]["auto_messages"][str(msg_id)]["title"] = title
                
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
            await ctx.send(f"Created a new Auto Announcer Message!\nThe ID for this is ``{msg_id}``, use this to edit the title and message.")
        except:
            raise
            await ctx.send(INVALID_DATABASE_ERROR)

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def del_msg(self, ctx, msg_id: int):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            del servers[str(ctx.message.guild.id)]["auto_messages"][str(msg_id)]
                
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
            await ctx.send(f"Deleted {msg_id}")
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def edit_msg_title(self, ctx, msg_id: int, *, title: str):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            servers[str(ctx.message.guild.id)]["auto_messages"][str(msg_id)]["title"] = title
                
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
            await ctx.send(f"Edited the title in {msg_id}")
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def edit_msg_desc(self, ctx, msg_id: int, *, desc: str):
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            servers[str(ctx.message.guild.id)]["auto_messages"][str(msg_id)]["desc"] = desc
                
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
            await ctx.send(f"Edited the desc in {msg_id}")
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

    @announcer.command()
    @commands.has_guild_permissions(administrator=True)
    async def messages(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)
                
            await ctx.send(servers[str(ctx.message.guild.id)]["auto_messages"])
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(trigger_cmd(bot))