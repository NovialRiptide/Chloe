import discord
import asyncio
from discord.ext import commands
from locals import *

pending_tasks = {}


class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if hasattr(message.channel, "guild"):
            channel = message.channel
            is_a_session_channel = channel.id in SESSION_CHANNELS

            if is_a_session_channel:
                for word in message.content.split(" "):
                    if word in CLOSE_KEYWORDS:
                        await message.channel.send(
                            "It seems like you're done here and saying your goodbyes and thanks.\nIf you would like to close this session, do `;close`. (Only the sesion creator can do this)"
                        )

            channel_history = await channel.history(limit=2).flatten()

            available_category = discord.utils.get(
                self.client.get_all_channels(), id=AVAILABLE_CATEGORY_ID
            )
            occupied_category = discord.utils.get(
                self.client.get_all_channels(), id=OCCUPIED_CATEGORY_ID
            )
            dormant_category = discord.utils.get(
                self.client.get_all_channels(), id=DORMANT_CATEGORY_ID
            )

            if (
                is_a_session_channel
                and channel.category_id == AVAILABLE_CATEGORY_ID
                and channel_history[0].author.id != self.client.user.id
                and message.guild.get_role(IN_SESSION_ROLE) not in message.author.roles
            ):
                await channel.edit(
                    category=occupied_category,
                    sync_permissions=True,
                    topic=f"{message.author.id}",
                )
                await channel_history[1].edit(
                    content=tsc_ongoing_session(message.author.mention)
                )
                await message.author.add_roles(channel.guild.get_role(IN_SESSION_ROLE))

                # takes a dormant session and makes it available
                if len(available_category.channels) <= MAX_NUMBER_OF_AVAILABLE_SESSIONS:
                    channel = dormant_category.channels[-1]
                    channel_history = await channel.history(limit=1).flatten()
                    await channel.edit(
                        category=available_category, sync_permissions=True
                    )
                    await channel_history[0].edit(
                        content=tsc_ongoing_session("")
                        + "To get started, speak in this channel to start your session."
                    )

            # IF SOMEHOW A PERSON WHO HAS ALREADY STARTED A SESSION CAN SEE OTHER AVAILABLE SESSIONS,
            # IT WILL AUTO DELETE THEIR MESSAGE TO PREVENT ANOTHER SESSION FROM STARTING UP
            elif (
                is_a_session_channel
                and channel.category_id == AVAILABLE_CATEGORY_ID
                and message.guild.get_role(IN_SESSION_ROLE) in message.author.roles
            ):
                await message.delete()

            # THIS IS SUPPOSE TO CHECK WHETHER A USER HAS SPOKEN IN AN ONGOING SESSION
            # IF THEY DID, THE TASK THAT IS MEANT TO AUTOCLOSE THE CHANNEL WILL RESET
            channel = message.channel
            is_a_session_channel = channel.id in SESSION_CHANNELS
            channel_history = await channel.history(limit=2).flatten()

            occupied_category = discord.utils.get(
                self.client.get_all_channels(), id=OCCUPIED_CATEGORY_ID
            )
            dormant_category = discord.utils.get(
                self.client.get_all_channels(), id=DORMANT_CATEGORY_ID
            )

            if (
                is_a_session_channel
                and channel.category_id == OCCUPIED_CATEGORY_ID
                and channel_history[0].author.id != self.client.user.id
            ):

                def check(ms):
                    return ms.channel.id in occupied_category.channels

                try:
                    if channel in pending_tasks:
                        pending_tasks[channel].close()
                    pending_tasks[channel] = self.client.wait_for(
                        "message", check=check, timeout=60 * 60
                    )
                    msg = await pending_tasks[channel]
                except asyncio.TimeoutError:
                    channel_history = await channel.history(limit=1).flatten()

                    member = message.guild.get_member(int(channel.topic))
                    try:
                        await (member).remove_roles(
                            channel.guild.get_role(IN_SESSION_ROLE)
                        )
                    except:
                        pass
                    await channel.edit(
                        category=dormant_category, sync_permissions=True, topic=""
                    )
                    await channel.send(
                        "**This channel has expired, so it has been marked as dormant.**\nPlease do not speak in this if you have permission to speak. If you think you can solve the user's issue, please DM them."
                    )
        else:
            pass


def setup(client):
    client.add_cog(sessions(client))
