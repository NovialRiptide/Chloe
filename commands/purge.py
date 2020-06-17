import discord
from discord.ext import commands
from vars import *

class purge_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(manage_messages=True)
    async def purge(self, ctx, number: int):
        if ctx.message.author.id in MEMBERS_WITH_PERMS:
            channel = ctx.message.channel
            await channel.purge(limit=number+1)
            await channel.send(f"Purged!")
        else:
            channel = ctx.message.channel
            await channel.send(f"You do not have permission to do that, {ctx.message.author}...")

def setup(bot):
    bot.add_cog(purge_cmd(bot))