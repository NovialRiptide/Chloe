import discord
import logging
import traceback
from discord.ext import commands

TOKEN = "NzE2Nzk2MDYyOTUzNjM1OTQx.XuGszw.1MCUZVqqmlOjS1nYYuPa7nJ5fnI"

client = commands.Bot(command_prefix="!")

logging.basicConfig(level="INFO")
logger = logging.getLogger("main.py")

extensions = [
    "events.on_error",
    #"events.on_invite_create",
    #"events.on_invite_delete",
    #"events.on_member_ban",
    #"events.on_member_join",
    #"events.on_member_remove",
    #"events.on_member_unban",
    #"events.on_message_delete",
    #"events.on_message_edit",
    "events.on_ready",

    #"commands.ban",
    "commands.channel_setup",
    "commands.json_database",
    #"commands.kick",
    "commands.ping",
    "commands.say",
    #"commands.purge",
    "commands.setup",
    "commands.tsc_rep",
    #"commands.unban",

    "auto_announcer.eventhandler",
    "auto_announcer.trigger",

    "sessions.close_cmd",
    "sessions.debug_cmd",
    "events.on_message",
    "sessions.session_setup"
]

for extension in extensions:
    try:
        client.load_extension(extension)
    except Exception:
        logger.error(f'Failed to load {extension} with error:\n{traceback.format_exc()}')

client.run(TOKEN)
