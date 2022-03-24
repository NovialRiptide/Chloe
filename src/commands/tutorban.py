import discord
from discord.ext import commands
from locals import *


class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(ban_members=True)
    async def tutorban(
        self, ctx, member: discord.Member, *, reason="No reason provided"
    ):
        try:
            for role in TUTOR_ROLES:
                await member.remove_roles(ctx.guild.get_role(TUTOR_ROLES[role]))
            await member.remove_roles(ctx.guild.get_role(MAIN_TUTOR_ROLE))
            await member.add_roles(ctx.guild.get_role(BANNED_ASSIGN_TUTOR_ROLE))
        except:
            raise

        await member.send(f"{ctx.author} has restricted you from becoming a tutor.")
        await ctx.send(
            f"Restricted {member.mention} from becoming a tutor for ``{reason}``"
        )


def setup(bot):
    bot.add_cog(sessions(bot))
