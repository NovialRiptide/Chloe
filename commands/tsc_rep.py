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
                
            async def upvote():
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["upvotes"] += 1
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"].append(ctx.author.id)

            if ctx.author.id != member.id:
                try:
                    if ctx.author.id in servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"]:
                        await ctx.send(f"You have already affected {member.name}'s reputation!")
                    else:
                        await upvote()
                        await ctx.send(f"You have upvoted {member.name}!")
                except KeyError:
                    servers[str(ctx.guild.id)]["reputation"][str(member.id)] = template
                    await upvote()
                    await ctx.send(f"You have upvoted {member.name}!")
            else:
                await ctx.send("Now why would you do that..")
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
                
            async def downvote():
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["downvotes"] += 1
                servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"].append(ctx.author.id)

            if ctx.author.id != member.id:
                try:
                    if ctx.author.id in servers[str(ctx.guild.id)]["reputation"][str(member.id)]["members_already_voted"]:
                        await ctx.send(f"You have already affected {member.name}'s reputation!")
                    else:
                        await downvote()
                        await ctx.send(f"You have downvoted {member.name}!")
                except KeyError:
                    servers[str(ctx.guild.id)]["reputation"][str(member.id)] = template
                    await downvote()

                await ctx.send(f"You have downvoted {member.name}!")
            else:
                await ctx.send("Now why would you do that..")

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
            async def print_rep():
                quote = QUOTES[random.randint(0, len(QUOTES)-1)]
                rep_data = servers[str(ctx.guild.id)]["reputation"][str(member.id)]
                embed=discord.Embed(title=f"{member}'s profile", description=f"{quote}")
                embed.add_field(name="Reputation", value=f"{rep_data['upvotes']-rep_data['downvotes']} (+{rep_data['upvotes']}/-{rep_data['downvotes']})", inline=False)

                await ctx.send(embed=embed)

            try:
                await print_rep()
            except KeyError:
                servers[str(ctx.guild.id)]["reputation"][str(member.id)] = template
                await print_rep()
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(rep_cmd(bot))