import discord
import time
from discord.ext import commands
from vars import *

class ping_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self, ctx):
        start_time = time.monotonic()
        message = await ctx.send("Pinging!")
        time_taken = time.monotonic() - start_time
       
        await message.edit(content=f"Ping! {time_taken * 1000:,.2f}ms")

def setup(bot):
    bot.add_cog(ping_cmd(bot))