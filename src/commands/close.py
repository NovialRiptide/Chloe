import discord
from discord.ext import commands
from locals import *


class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def close(self, ctx):
        server_management_role = ctx.guild.get_role(630180904920285194)
        if (
            int(ctx.channel.topic) == ctx.author.id
            or server_management_role in ctx.author.roles
        ):
            is_a_session_channel = ctx.channel.id in SESSION_CHANNELS
            available_category = discord.utils.get(
                self.client.get_all_channels(), id=AVAILABLE_CATEGORY_ID
            )
            occupied_category = discord.utils.get(
                self.client.get_all_channels(), id=OCCUPIED_CATEGORY_ID
            )
            dormant_category = discord.utils.get(
                self.client.get_all_channels(), id=DORMANT_CATEGORY_ID
            )

            if is_a_session_channel and ctx.channel.category_id == OCCUPIED_CATEGORY_ID:
                member = ctx.guild.get_member(int(ctx.channel.topic))
                try:
                    await member.remove_roles(
                        ctx.channel.guild.get_role(IN_SESSION_ROLE)
                    )
                except:
                    pass
                await ctx.channel.edit(
                    category=dormant_category, sync_permissions=True, topic=""
                )
                await ctx.channel.send(
                    "**This channel has been marked as dormant.**\nThis channel is not meant to be in use."
                )
        else:
            await channel.send(
                f"You do not have permission to do that, only someone with the ``{server_management_role}`` role can."
            )


def setup(bot):
    bot.add_cog(sessions(bot))
