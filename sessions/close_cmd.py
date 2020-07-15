import discord
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def close(self, ctx):
        try:
            channel = ctx.channel
            role = MAIN_TUTOR_ROLE
            if ctx.guild.get_role(role) in ctx.author.roles or int(channel.topic) == ctx.author.id:
                is_a_session_channel = channel.id in SESSION_CHANNELS
                available_category = discord.utils.get(self.client.get_all_channels(), id=AVAILABLE_CATEGORY_ID)
                occupied_category = discord.utils.get(self.client.get_all_channels(), id=OCCUPIED_CATEGORY_ID)
                dormant_category = discord.utils.get(self.client.get_all_channels(), id=DORMANT_CATEGORY_ID)

                if is_a_session_channel and channel.category_id == OCCUPIED_CATEGORY_ID:
                    member = ctx.guild.get_member(int(channel.topic))
                    await member.remove_roles(channel.guild.get_role(IN_SESSION_ROLE))
                    await channel.edit(category=dormant_category, sync_permissions=True, topic="")
                    await channel.send("**This channel has been marked as dormant.**\nThis channel is not meant to be in use.")
            else:
                await channel.send(f"You do not have permission to do that, only someone with the ``{ctx.guild.get_role(role)}`` role can.")
        except:
            raise
            pass

def setup(bot):
    bot.add_cog(sessions(bot))