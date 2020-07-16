import discord
import time
from discord.ext import commands
from vars import *

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def say(self, ctx, *, message: str):
        await ctx.send(message)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(fun(bot))