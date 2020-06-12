import discord
import json
from discord.ext import commands
from vars import *

class sessions(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def set_session_category(self, ctx, json_key: str, category_id: int):
        try:
            if json_key in VALID_SESSION_CATEGORIES:
                with open("servers.json") as f:
                    servers = json.load(f)
                server = servers[str(ctx.guild.id)]
                server["session_categories"][json_key] = category_id
                await ctx.send(f"``{json_key}`` is now assigned ``{category_id}``")
                with open("servers.json", "w") as json_file:
                    json.dump(servers, json_file)
        except:
            raise
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(sessions(bot))