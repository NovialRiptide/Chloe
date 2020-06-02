import discord
import time
from discord.ext import commands
from vars import *

class kick_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason: str):
        if ctx.message.author.id in MEMBERS_WITH_PERMS or ctx.message.author == ctx.message.guild.owner:
            channel = ctx.message.channel
            embed=discord.Embed(
                color=0xff0000, 
                title=f"Kick Executed: [{member}] by {ctx.message.author}",
                description=f"Reason: {reason}"
            )
            await channel.send(embed=embed)
            channel = self.client.get_channel(JOIN_LEAVE_CHANNEL)
            await channel.send(embed=embed)

            embed=discord.Embed(
                color=0xff0000, 
                title=f"You have been kicked by {ctx.message.author} in {ctx.message.guild}",
                description=f"Reason: {reason}"
            )
            await member.send(embed=embed)
            await member.kick(reason=reason)

            channel = self.client.get_channel(LOGGING_CHANNEL)
            await channel.send(embed=embed)
        else:
            channel = ctx.message.channel
            await channel.send(f"You do not have permission to do that, {ctx.message.author}...")
            channel = self.client.get_channel(LOGGING_CHANNEL)
            embed=discord.Embed(
                color=0xff0000, 
                title=f"Kick Attempt: [{member}] by {ctx.message.author}",
                description=f"Reason: {reason}"
            )
            await channel.send(embed=embed)

def setup(bot):
    bot.add_cog(kick_cmd(bot))