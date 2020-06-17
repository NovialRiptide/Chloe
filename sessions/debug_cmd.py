import discord
import json
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def debug(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            channel = ctx.channel
            is_a_session_channel = channel.id in servers[str(channel.guild.id)]["channels"]["sessions"]

            available_category_id = servers[str(channel.guild.id)]["session_categories"]["available"]
            available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
            available_category_channels = available_category.text_channels

            occupied_category_id = servers[str(channel.guild.id)]["session_categories"]["occupied"]
            occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
            occupied_category_channels = occupied_category.text_channels

            dormant_category_id = servers[str(channel.guild.id)]["session_categories"]["dormant"]
            dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)
            dormant_category_channels = dormant_category.text_channels

            role_being_helped = ctx.guild.get_role(servers[str(channel.guild.id)]["in_session_role"])
            helper = ctx.guild.get_role(servers[str(channel.guild.id)]["session_helper_role"])

            await available_category.set_permissions(ctx.guild.default_role, read_messages=True, send_messages=True)
            await available_category.set_permissions(role_being_helped, read_messages=True, send_messages=False)

            await occupied_category.set_permissions(ctx.guild.default_role, send_messages=False, read_messages=False)
            await occupied_category.set_permissions(role_being_helped, send_messages=True, read_messages=True)
            await occupied_category.set_permissions(helper, send_messages=True, read_messages=True)

            await dormant_category.set_permissions(ctx.guild.default_role, send_messages=False)
            await dormant_category.set_permissions(helper, send_messages=False)
            await ctx.channel.send("Finished! (MAKE SURE YOU TURNED ON SYNC FOR ALL THE CHANNELS)")

        except:
            raise
            pass

def setup(bot):
    bot.add_cog(sessions(bot))