import json
import discord
from discord.ext import commands
from vars import *

class fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    @commands.has_guild_permissions()
    async def dontasktoask(self, ctx):
        message = "Every now and then, someone pops in and says something in the lines of, ```Any XNA experts around?``` This is bad form, for several reasons. What the person is actually asking here is, ```Any XNA experts around who are willing to commit into looking into my problem, whatever that may turn out to be, even if it's not actually related to XNA or if someone who doesn't know anything about XNA could actually answer my question?``` There are plenty of reasons why people who DO have the knowledge would not admit to it. By asking, you're asking for more than what you think you're asking.\n\nYou're asking people to take responsibility. You're questioning people's confidence in their abilities. You're also unnecessarily walling other people out. I often answer questions related to languages or libraries I have never used, because the answers are (in a programmer kind of way) common sense.\n\nAlternatively, it can be seen as.. ```I have a question about XNA but I'm too lazy to actually formalize it in words unless there's someone on the channel who might be able to answer it. ``` ..which is just lazy. If you're not willing to do the work to solve your problem, why should we?\n\nThe solution is not to ask to ask, but just to ask. Someone who is idling on the channel and only every now and then glances what's going on is unlikely to answer to your \"asking to ask\" question, but your actual problem description may pique their interest and get them to answer.\n\nSo, to repeat: Don't ask to ask. Just ask."
        embed=discord.Embed(title="Don't ask to ask. Just ask.", url="http://sol.gfxile.net/dontask.html", description=message)
        embed.set_footer(text=f"{ctx.author} wants you to read this.")
        await ctx.channel.send(embed=embed)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(fun(bot))
