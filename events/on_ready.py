import discord
from discord.ext import commands

class on_ready_event(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Game(name="The Study Corner Bot"))
        print(f"Logged on as {self.client.user}!")

def setup(client):
    client.add_cog(on_ready_event(client))