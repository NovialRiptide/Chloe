import discord
import traceback
from discord.ext import commands

async def find_session_user(client, channel, limit):
    return channel.topic