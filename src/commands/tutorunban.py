import discord
from discord.ext import commands
from locals import *


class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def tutorunban(
        self, ctx, member: discord.Member, *, reason="No reason provided"
    ):
        try:
            await member.remove_roles(ctx.guild.get_role(BANNED_ASSIGN_TUTOR_ROLE))
        except:
            pass

        await member.send(f"{ctx.author} has unrestricted you from becoming a tutor.")
        await ctx.send(
            f"Unrestricted {member.mention} from becoming a tutor for ``{reason}``"
        )


def setup(bot):
    bot.add_cog(sessions(bot))
