import discord
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def tutorban(self, ctx, member: discord.Member, *, reason):
        try:
            for role in TUTOR_ROLES:
                await ctx.author.remove_roles(ctx.guild.get_role(role))
            await ctx.author.remove_roles(ctx.guild.get_role(MAIN_TUTOR_ROLE))
        except: pass

        await member.send(f"{ctx.author} has restricted you from becoming a tutor.")
        await ctx.send(f"Restricted {member.mention} from becoming a tutor for {reason}")

def setup(bot):
    bot.add_cog(sessions(bot))