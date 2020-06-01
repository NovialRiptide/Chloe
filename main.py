import discord
from discord.ext import commands

TOKEN = "NzE2Nzk2MDYyOTUzNjM1OTQx.XtQ_jg.Ezd74DZ2cJ9vj7Qw_6gSicwQbKo"

JOIN_LEAVE_CHANNEL = 716801483533844571
LOGGING_CHANNEL = 716810086852329553

MEMBERS_WITH_PERMS = [182288858782629888]

client = commands.Bot(command_prefix="!")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="prefix: !"))
    print(f"Logged on as {client.user}!")

@client.event
async def on_member_join(member):
    channel = client.get_channel(JOIN_LEAVE_CHANNEL)
    embed=discord.Embed(
        color=0x0080ff,
        title=f"{member} has joined the server", 
        description=f"User ID: {member.id}"
    )
    await channel.send(embed=embed)

@client.event
async def on_member_remove(member):
    channel = client.get_channel(JOIN_LEAVE_CHANNEL)
    embed=discord.Embed(
        color=0x0080ff,
        title=f"{member} has left/been banned the server", 
        description=f"User ID: {member.id}"
    )
    await channel.send(embed=embed)

@client.event
async def on_member_unban(server, member):
    channel = client.get_channel(JOIN_LEAVE_CHANNEL)
    embed=discord.Embed(
        color=0x0080ff,
        title=f"{member} has been unbanned the server", 
        description=f"User ID: {member.id}"
    )
    await channel.send(embed=embed)

@client.event
async def on_invite_create(invite):
    channel = client.get_channel(LOGGING_CHANNEL)
    embed=discord.Embed(
        color=0xff0000, 
        title=f"Invite Created: [{invite.inviter}]",
        description=f"Max Age: {invite.max_age} seconds\nUses: {invite.uses}\nMax Uses: {invite.max_uses}\nCode: {invite.code}"
    )
    await channel.send(embed=embed)

@client.event
async def on_invite_delete(invite):
    channel = client.get_channel(LOGGING_CHANNEL)
    embed=discord.Embed(
        color=0xff0000, 
        title=f"Invite Deleted: [N/A]",
        description=f"Code: {invite.code}"
    )
    await channel.send(embed=embed)

@client.event
async def on_message_edit(before, after):
    channel = client.get_channel(LOGGING_CHANNEL)
    embed=discord.Embed(
        color=0xff0000, 
        title=f"Message Edited: [{before.author}] in #{before.channel}",
        description=f"Before: {before.content}\nAfter: {after.content}"
    )
    if before.author != client.user:
        await channel.send(embed=embed)

@client.event
async def on_message_delete(message):
    channel = client.get_channel(LOGGING_CHANNEL)
    embed=discord.Embed(
        color=0xff0000, 
        title=f"Message Deleted: [{message.author}] in #{message.channel}",
        description=f"Contents: {message.content}"
    )
    await channel.send(embed=embed)
    
@client.command()
async def purge(ctx, number: int):
    if ctx.message.author.id in MEMBERS_WITH_PERMS:    
        channel = ctx.message.channel
        await channel.purge(limit=number+1)
        channel = client.get_channel(LOGGING_CHANNEL)
        embed=discord.Embed(
            color=0xff0000, 
            title=f"Purge: [{ctx.message.author}] in #{ctx.message.channel}",
            description=f"Message(s) Purged: {number}"
        )
        await channel.send(embed=embed)
    else:
        channel = ctx.message.channel
        await channel.send(f"You do not have permission to do that, {ctx.message.author}...")
        channel = client.get_channel(LOGGING_CHANNEL)
        embed=discord.Embed(
            color=0xff0000, 
            title=f"Purge Attempt: [{ctx.message.author}] in #{ctx.message.channel}"
        )
        await channel.send(embed=embed)

client.run(TOKEN)