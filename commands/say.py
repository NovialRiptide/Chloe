import discord
import time
from discord.ext import commands
from vars import *

class say_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, message: str):
        await ctx.send(message)

def setup(bot):
    bot.add_cog(say_cmd(bot))