import discord
from discord.ext import commands
from vars import *

class on_command_error_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        channel = ctx.message.channel
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(MISSING_ARGUMENTS_ERROR)
        elif isinstance(error, commands.TooManyArguments):
            await ctx.send(TOO_MANY_ARGUMENTS_ERROR)
        elif isinstance(error, commands.UserInputError):
            await ctx.send(USER_INPUT_ERROR)
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(NO_PERMISSION_ERROR)
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(BOT_NO_PERMISSION_ERROR)
        elif isinstance(error, commands.CommandNotFound): pass
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
        else:
            await ctx.send(f"Send this to the developer.```{error}```")

def setup(client):
    client.add_cog(on_command_error_event(client))