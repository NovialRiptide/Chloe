import discord
import time
from discord.ext import commands
from vars import *

class unban_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, id: int, *, reason: str):
        member = discord.Object(id=id)
        if ctx.message.author.id in MEMBERS_WITH_PERMS or ctx.message.author == ctx.message.guild.owner:
            channel = ctx.message.channel
            guild = ctx.message.guild
            embed=discord.Embed(
                color=0xff0000, 
                title=f"Unban Executed: [{id}] by {ctx.message.author}",
                description=f"Reason: {reason}"
            )
            await channel.send(embed=embed)
            await guild.unban(member, reason=reason)

            channel = self.client.get_channel(LOGGING_CHANNEL)
            await channel.send(embed=embed)
        else:
            channel = ctx.message.channel
            await channel.send(f"You do not have permission to do that, {ctx.message.author}...")
            channel = self.client.get_channel(LOGGING_CHANNEL)
            embed=discord.Embed(
                color=0xff0000, 
                title=f"Unban Attempt: [{id}] by {ctx.message.author}",
                description=f"Reason: {reason}"
            )
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(unban_cmd(bot))