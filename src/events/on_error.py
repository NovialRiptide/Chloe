import discord
from discord.ext import commands
from locals import *

MISSING_ARGUMENTS_ERROR = "You are missing some arguments..."
TOO_MANY_ARGUMENTS_ERROR = "You have too many arguments!"
USER_INPUT_ERROR = "You have inputted your arguments wrong!"
NO_PERMISSION_ERROR = "You do not have permission to do this..."
BOT_NO_PERMISSION_ERROR = "I do not have permission to do this..."
UNKNOWN_COMMAND_ERROR = "I have never heard of this command before."
FAKE_ERROR = "An error has occurred. Please try again later."


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
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(error)
        else:
            await ctx.send(
                f"Uh oh! An error occured.```{error}``` <@695502565668028468>"
            )


def setup(client):
    client.add_cog(on_command_error_event(client))
