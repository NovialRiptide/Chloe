import discord
import json
import random
from discord.ext import commands
from vars import *

class rep_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["rep"])
    async def reputation(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(MISSING_ARGUMENTS_ERROR)
            
    @reputation.command()
    @commands.has_guild_permissions(administrator=True)
    async def setup(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            
            if "reputation" in list(servers[str(ctx.guild.id)]):
                await ctx.send("This has already been implemented")
            else:
                servers[str(ctx.guild.id)]["reputation"] = {}
                await ctx.send("Reputation system has been implemented!")

            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            raise
            await ctx.send(INVALID_DATABASE_ERROR)

    @reputation.command(aliases=["praise","upvote"])
    async def give(self, ctx, member: discord.Member):
        template = {"upvotes": 0, "downvotes": 0, "members_already_voted": []}
        try:
            with open("servers.json") as f:
                servers = json.load(f)
                
            try:
                if ctx.author.id in servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"]:
                    await ctx.send(f"You have already affected {member.name}'s reputation!")
                else:
                    servers[str(ctx.guild.id)]["reputation"][str(member.id)]["upvotes"] += 1
                    servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"].append(ctx.author.id)
                    await ctx.send(f"You have upvoted {member.name}!")
            except KeyError:
                servers[str(ctx.guild.id)]["reputation"][str(member.id)] = template
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["upvotes"] += 1
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"].append(ctx.author.id)

                await ctx.send(f"You have upvoted {member.name}!")
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            raise
            await ctx.send(INVALID_DATABASE_ERROR)

    @reputation.command(aliases=["downvote"])
    async def remove(self, ctx, member: discord.Member):
        template = {"upvotes": 0, "downvotes": 0, "members_already_voted": []}
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            try:
                if ctx.author.id in servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"]:
                    await ctx.send(f"You have already affected {member.name}'s reputation!")
                else:
                    servers[str(ctx.guild.id)]["reputation"][str(member.id)]["downvotes"] += 1
                    servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"].append(ctx.author.id)
                    await ctx.send(f"You have downvoted {member.name}!")
            except KeyError:
                servers[str(ctx.guild.id)]["reputation"][str(member.id)] = template
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["downvotes"] += 1
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"].append(ctx.author.id)

                await ctx.send(f"You have downvoted {member.name}!")
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

    @reputation.command()
    async def show(self, ctx, member: discord.Member):
        template = {"upvotes": 0, "downvotes": 0, "members_already_voted": []}
        try:
            with open("servers.json") as f:
                servers = json.load(f)

            try:
                await ctx.send(servers[str(ctx.guild.id)]["reputation"][str(member.id)])
            except KeyError:
                servers[str(ctx.guild.id)]["reputation"][str(member.id)] = template

                await ctx.send(servers[str(ctx.guild.id)]["reputation"][str(member.id)])
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(rep_cmd(bot))