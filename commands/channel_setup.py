import discord
import json
from discord.ext import commands
from vars import *

class channel_setup(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_guild_permissions(administrator=True)
    async def set_channel(self, ctx, json_key: str, channel: discord.TextChannel):
        try:
            if json_key in list(VALID_CHANNEL_JSON_KEYS):
                with open("servers.json") as f:
                    servers = json.load(f)
                server = servers[str(ctx.guild.id)]
                id = channel.id
                if VALID_CHANNEL_JSON_KEYS[json_key] == "int":
                    server["channels"][json_key] = id
                    await ctx.send(f"``{json_key}`` is now assigned ``{id}``")
                elif VALID_CHANNEL_JSON_KEYS[json_key] == "list":
                    try:
                        server["channels"][json_key].append(id)
                        await ctx.send(f"``{json_key}`` is now assigned ``{id}``")
                    except:
                        server["channels"][json_key] = []
                        server["channels"][json_key].append(id)
                        await ctx.send(f"``{json_key}`` is now assigned ``{id}``")
                with open("servers.json", "w") as json_file:
                    json.dump(servers, json_file)
        except:
            raise
            await ctx.send(INVALID_DATABASE_ERROR)

def setup(bot):
    bot.add_cog(channel_setup(bot))