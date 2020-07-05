import discord
import json
from mee6_py_api import API
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def assign(self, ctx, subject: str):
        if subject.upper() in TUTOR_ROLES.keys():
            if ctx.guild.get_role(MAIN_TUTOR_ROLE) not in ctx.author.roles:
                await ctx.author.add_roles(ctx.guild.get_role(MAIN_TUTOR_ROLE))
            await ctx.author.add_roles(ctx.guild.get_role(TUTOR_ROLES[subject.upper()]))
            await ctx.send(f"You became a {subject} tutor!")
        else:
            await ctx.send(f"That's an invalid tutor role\nHere are the avaliable roles: ``{TUTOR_ROLES.keys()}``")

def setup(bot):
    bot.add_cog(sessions(bot))