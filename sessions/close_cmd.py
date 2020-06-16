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
            channel = ctx.channel
            with open("servers.json") as f:
                servers = json.load(f)
            role = servers[str(channel.guild.id)]["session_helper_role"]
            if ctx.guild.get_role(role) in ctx.author.roles:
                is_a_session_channel = channel.id in servers[str(channel.guild.id)]["channels"]["sessions"]

                available_category_id = servers[str(channel.guild.id)]["session_categories"]["available"]
                available_category = discord.utils.get(self.client.get_all_channels(), id=available_category_id)
                occupied_category_id = servers[str(channel.guild.id)]["session_categories"]["occupied"]
                occupied_category = discord.utils.get(self.client.get_all_channels(), id=occupied_category_id)
                dormant_category_id = servers[str(channel.guild.id)]["session_categories"]["dormant"]
                dormant_category = discord.utils.get(self.client.get_all_channels(), id=dormant_category_id)

                if is_a_session_channel and channel.category_id == occupied_category_id:
                    embed=discord.Embed(
                        title=f"This channel has been marked as dormant",
                        description=f"If you're a staff member and you have permission to speak in this channel, do not do it! It will break the bot!"
                    )
                    async def find_session_user(limit):
                        async for message in channel.history(limit=limit):
                            if message.author == self.client.user:
                                try:
                                    return int(message.embeds[0].footer.text)
                                except IndexError:
                                    pass
                        await find_session_user(limit*2)

                    member = ctx.guild.get_member(await find_session_user(50))
                    await member.remove_roles(channel.guild.get_role(servers[str(ctx.guild.id)]["in_session_role"]))
                    await channel.edit(category=dormant_category, sync_permissions=True)
                    await channel.send(embed=embed)
            else:
                await channel.send(f"You do not have permission to do that, only someone with the ``{ctx.guild.get_role(role)}`` role can.")
        except:
            raise
            pass

def setup(bot):
    bot.add_cog(sessions(bot))