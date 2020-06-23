import json
import discord
from discord.ext import commands
from vars import *

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions()
    async def dontasktoask(self, ctx):
        await ctx.channel.send(f"{ctx.author.mention} wants you to read this: http://sol.gfxile.net/dontask.html")

def setup(bot):
    bot.add_cog(fun(bot))