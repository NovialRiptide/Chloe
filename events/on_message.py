import discord
import asyncio
from discord.ext import commands
from vars import *

pending_tasks = {}

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if hasattr(message.channel, "guild"):
            for member_id in PING_REE:
                try:
                    if message.guild.get_member(member_id) in message.mentions:
                        await message.add_reaction(self.client.get_emoji(644393169873534977))
                except AttributeError: pass
            
            try:
                channel = message.channel
                is_a_session_channel = channel.id in SESSION_CHANNELS
                channel_history = await channel.history(limit=2).flatten()

                available_category = discord.utils.get(self.client.get_all_channels(), id=AVAILABLE_CATEGORY_ID)
                occupied_category = discord.utils.get(self.client.get_all_channels(), id=OCCUPIED_CATEGORY_ID)
                dormant_category = discord.utils.get(self.client.get_all_channels(), id=DORMANT_CATEGORY_ID)

                if is_a_session_channel and channel.category_id == AVAILABLE_CATEGORY_ID and channel_history[0].author.id != self.client.user.id and message.guild.get_role(IN_SESSION_ROLE) not in message.author.roles:
                    await channel.edit(category=occupied_category, sync_permissions=True, topic=f"{message.author.id}")
                    await channel_history[1].edit(content=tsc_ongoing_session(message.author.mention))
                    await message.author.add_roles(channel.guild.get_role(IN_SESSION_ROLE))

                    if len(available_category.channels) <= MAX_NUMBER_OF_AVAILABLE_SESSIONS:
                        channel = dormant_category.channels[-1]
                        channel_history = await channel.history(limit=1).flatten()
                        await channel.edit(category=available_category, sync_permissions=True)
                        await channel_history[0].edit(content="Speak in this channel to start your tutor session!")

                elif is_a_session_channel and channel.category_id == AVAILABLE_CATEGORY_ID and message.guild.get_role(IN_SESSION_ROLE) in message.author.roles:
                    await message.delete()
                
                # THIS IS SUPPOSE TO CHECK WHETHER A USER HAS SPOKEN IN AN ONGOING SESSION
                # IF THEY DID, THE TASK THAT IS MEANT TO AUTOCLOSE THE CHANNEL WILL RESET
                channel = message.channel
                is_a_session_channel = channel.id in SESSION_CHANNELS
                channel_history = await channel.history(limit=2).flatten()

                available_category = discord.utils.get(self.client.get_all_channels(), id=AVAILABLE_CATEGORY_ID)
                occupied_category = discord.utils.get(self.client.get_all_channels(), id=OCCUPIED_CATEGORY_ID)
                dormant_category = discord.utils.get(self.client.get_all_channels(), id=DORMANT_CATEGORY_ID)

                if is_a_session_channel and channel.category_id == OCCUPIED_CATEGORY_ID and channel_history[0].author.id != self.client.user.id:
                    def check(ms):
                        return ms.channel.id in occupied_category.channels
                    try:
                        if channel in pending_tasks:
                            pending_tasks[channel].close()
                        pending_tasks[channel] = self.client.wait_for("message", check=check, timeout=60*30)
                        msg = await pending_tasks[channel]
                    except asyncio.TimeoutError:
                        channel_history = await channel.history(limit=1).flatten()

                        member = message.guild.get_member(int(channel.topic))
                        await (member).remove_roles(channel.guild.get_role(IN_SESSION_ROLE))
                        await channel.edit(category=dormant_category, sync_permissions=True, topic="")
                        await channel.send("**This channel has been marked as dormant.**\nPlease do not speak in this if you have permission to speak.")
                        await member.send("Your session has expired in **The Study Corner**")
            except:
                raise
                pass
        else: pass

def setup(client):
    client.add_cog(sessions(client))