import discord
import json
from discord.ext import commands
from vars import *

class json_cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def database(self, ctx):
        try:
            with open("servers.json") as f:
                servers = json.load(f)
                
            await ctx.send(f"```{servers[str(ctx.message.guild.id)]}``````VALID JSON KEYS\n{list(VALID_CHANNEL_JSON_KEYS)}```")
        except:
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(json_cmd(bot))