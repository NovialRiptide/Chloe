import discord
from discord.ext import commands
from locals import *


class miscellaneous(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def about(self, ctx):
        embed = discord.Embed(
            title="Kenji",
            url="https://github.com/anbdrew/Kenji",
            description=f"My sole purpose is to manage sessions to ensure that you will have a session to yourself while no one else is going to intervene.```bot stats\n - last update: {LAST_UPDATE_DATE}\n - build #: {BUILD_NUMBER}```",
        )
        embed.set_footer(text="Programmed by anbdrew (aka novial)")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(miscellaneous(bot))
