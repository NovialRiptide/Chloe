import discord
import json
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def debug(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            channel = ctx.channel
            is_a_session_channel = channel.id in servers[str(channel.guild.id)]["channels"]["sessions"]

            available_category_id = servers[str(channel.guild.id)]["session_categories"]["available"]
            available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
            occupied_category_id = servers[str(channel.guild.id)]["session_categories"]["occupied"]
            occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
            dormant_category_id = servers[str(channel.guild.id)]["session_categories"]["dormant"]
            dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)

            available_category_channels = len(available_category.channels)
            occupied_category_channels = len(occupied_category.channels) 
            dormant_category_channels = len(dormant_category.channels)

            if available_category_channels < MAX_NUMBER_OF_AVAILABLE_SESSIONS:
                for x in range(MAX_NUMBER_OF_AVAILABLE_SESSIONS):
                    channel = dormant_category.channels[-1]
                    await channel.edit(category=available_category)
            channel = ctx.channel
            await channel.send("Debugging..")

        except:
            raise
            pass

def setup(bot):
    bot.add_cog(sessions(bot))