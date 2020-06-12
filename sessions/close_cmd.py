import discord
import json
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def close(self, ctx):
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

            if is_a_session_channel and channel.category_id == occupied_category_id:
                embed=discord.Embed(
                    title=f"session now dormant",
                    description=f"shit"
                )
                await channel.edit(category=dormant_category)
                await channel.send(embed=embed)
        except:
            pass

def setup(bot):
    bot.add_cog(sessions(bot))