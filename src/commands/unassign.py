import discord
from discord.ext import commands
from locals import *


class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def unassign(self, ctx, subject: str):
        if subject.upper() in TUTOR_ROLES.keys():
            await ctx.author.remove_roles(
                ctx.guild.get_role(TUTOR_ROLES[subject.upper()])
            )
            await ctx.send(f"You are not a {subject} tutor anymore!")
            do_anything = True
            for role in TUTOR_ROLES.keys():
                if ctx.guild.get_role(role) in ctx.author.roles:
                    do_anything = False

            if do_anything:
                await ctx.author.remove_roles(ctx.guild.get_role(MAIN_TUTOR_ROLE))
        else:
            await ctx.send(
                f"That's an invalid tutor role\nHere are the avaliable roles: ``{TUTOR_ROLES.keys()}``"
            )


def setup(bot):
    bot.add_cog(sessions(bot))
