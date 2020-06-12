import discord
import json
import asyncio
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        message_split = message.content.split(" ")
        channel = message.channel
        for word in BLACKLISTED_WORDS:
            if word in message_split:
                await channel.send("That's not nice..")
        
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            channel = message.channel
            is_a_session_channel = channel.id in servers[str(channel.guild.id)]["channels"]["sessions"]
            channel_history = await channel.history(limit=2).flatten()

            available_category_id = servers[str(channel.guild.id)]["session_categories"]["available"]
            available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
            occupied_category_id = servers[str(channel.guild.id)]["session_categories"]["occupied"]
            occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
            dormant_category_id = servers[str(channel.guild.id)]["session_categories"]["dormant"]
            dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)

            if is_a_session_channel and channel.category_id == available_category_id and channel_history[0].author.id != self.client.user.id:
                embed=discord.Embed(
                    title=f"session ongoing",
                    description=f"shit"
                )
                embed.set_footer(text=f"{message.author.id}")
                await channel.edit(category=occupied_category)
                await channel_history[1].edit(embed=embed)
                await message.author.add_roles(channel.guild.get_role(servers[str(message.guild.id)]["in_session_role"]))
                if len(available_category.channels) <= MAX_NUMBER_OF_AVAILABLE_SESSIONS:
                    embed=discord.Embed(
                        title=f"session available",
                        description=f"shit"
                    )
                    channel = dormant_category.channels[-1]
                    channel_history = await channel.history(limit=1).flatten()
                    await channel.edit(category=available_category)
                    await channel_history[0].edit(embed=embed)
                    
            channel = message.channel
            is_a_session_channel = channel.id in servers[str(channel.guild.id)]["channels"]["sessions"]
            channel_history = await channel.history(limit=2).flatten()

            available_category_id = servers[str(channel.guild.id)]["session_categories"]["available"]
            available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
            occupied_category_id = servers[str(channel.guild.id)]["session_categories"]["occupied"]
            occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
            dormant_category_id = servers[str(channel.guild.id)]["session_categories"]["dormant"]
            dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)
            if is_a_session_channel and channel.category_id == occupied_category_id and channel_history[0].author.id != self.client.user.id:
                check = message.channel.id in occupied_category.channels
                try:
                    await self.client.wait_for("message", check=check, timeout=60*5)
                except asyncio.TimeoutError:
                    embed=discord.Embed(
                        title=f"session now dormant",
                        description=f"shit"
                    )
                    async def find_session_user(limit):
                        async for message in channel.history(limit=limit):
                            if message.author == self.client.user:
                                try:
                                    return int(message.embeds[0].footer.text)
                                except IndexError:
                                    pass
                        await find_session_user(limit*2)

                    await (message.guild.get_member(await find_session_user(50))).remove_roles(channel.guild.get_role(servers[str(message.guild.id)]["in_session_role"]))
                    await channel.edit(category=dormant_category)
                    await channel.send(embed=embed)
        except:
            raise
            pass

def setup(client):
    client.add_cog(sessions(client))