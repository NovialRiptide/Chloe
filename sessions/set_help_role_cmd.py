import discord
import json
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def set_helper(self, ctx, role: discord.Role):
        try:
            with open("servers.json") as f:
                servers = json.load(f)
            server = servers[str(ctx.guild.id)]
            server["session_helper_role"] = role.id
            await ctx.send(f"``HELPER`` is now assigned to role ``{role}``")
            with open("servers.json", "w") as json_file:
                json.dump(servers, json_file)
        except:
            raise
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(sessions(bot))