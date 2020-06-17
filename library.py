import discord
from discord.ext import commands

async def find_session_user(client, channel, limit):
    async for message in channel.history(limit=limit):
        if message.author == client.user:
            try:
                return int(message.embeds[0].footer.text)
            except IndexError:
                pass
    await find_session_user(limit*2)