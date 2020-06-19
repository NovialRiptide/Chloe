import discord
import json
import asyncio
from discord.ext import commands
from vars import *
from library import *

pending_tasks = {}

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        for member_id in PING_REE:
            if message.guild.get_member(member_id) in message.mentions:
                await message.add_reaction(self.client.get_emoji(644393169873534977))
        
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            channel = message.channel
            server = servers[str(channel.guild.id)]
            is_a_session_channel = channel.id in server["channels"]["sessions"]
            channel_history = await channel.history(limit=2).flatten()

            available_category_id = server["session_categories"]["available"]
            available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
            occupied_category_id = server["session_categories"]["occupied"]
            occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
            dormant_category_id = server["session_categories"]["dormant"]
            dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)

            if is_a_session_channel and channel.category_id == available_category_id and channel_history[0].author.id != self.client.user.id and message.guild.get_role(server["in_session_role"]) not in message.author.roles:
                embed=discord.Embed(
                    title=f"Channel is now in session...",
                    description=tsc_ongoing_session(message.author.mention)
                )
                await channel.edit(category=occupied_category, sync_permissions=True, topic=f"{message.author.id}")
                await channel_history[1].edit(embed=embed)
                await message.author.add_roles(channel.guild.get_role(servers[str(message.guild.id)]["in_session_role"]))

                if len(available_category.channels) <= MAX_NUMBER_OF_AVAILABLE_SESSIONS:
                    embed=discord.Embed(
                        title=f"Session available",
                        description=f"Speak in this channel to start your tutor session!"
                    )
                    channel = dormant_category.channels[0]
                    channel_history = await channel.history(limit=1).flatten()
                    await channel.edit(category=available_category, sync_permissions=True)
                    await channel_history[0].edit(embed=embed)

            elif is_a_session_channel and channel.category_id == available_category_id and message.guild.get_role(server["in_session_role"]) in message.author.roles:
                await message.delete()
            
            # UPDATING THE VARIABLES BECAUSE THE CATEGORY OF THE CHANNEL HAS CHANGEDs AT THIS POINT IN TIME
            channel = message.channel
            is_a_session_channel = channel.id in server["channels"]["sessions"]
            channel_history = await channel.history(limit=2).flatten()

            available_category_id = server["session_categories"]["available"]
            available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
            occupied_category_id = server["session_categories"]["occupied"]
            occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
            dormant_category_id = server["session_categories"]["dormant"]
            dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)

            if is_a_session_channel and channel.category_id == occupied_category_id and channel_history[0].author.id != self.client.user.id:
                def check(ms):
                    return ms.channel.id in occupied_category.channels
                try:
                    if channel in pending_tasks:
                        pending_tasks[channel].close()
                    pending_tasks[channel] = self.client.wait_for("message", check=check, timeout=60*30)
                    msg = await pending_tasks[channel]
                except asyncio.TimeoutError:
                    channel_history = await channel.history(limit=1).flatten()

                    embed=discord.Embed(
                        title=f"This channel has been marked as dormant",
                        description=f"If you're a staff member and you have permission to speak in this channel, do not do it! It will break the bot!"
                    )
                    
                    await (message.guild.get_member(int(channel.topic))).remove_roles(channel.guild.get_role(servers[str(message.guild.id)]["in_session_role"]))
                    await channel.edit(category=dormant_category, sync_permissions=True, topic="")
                    await channel.send(embed=embed)
                    print(f"{channel.id} has closed on its own.")
        except:
            raise
            pass

def setup(client):
    client.add_cog(sessions(client))