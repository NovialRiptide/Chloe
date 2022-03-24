import discord
import logging
import traceback
from discord.ext import commands
from secret import TOKEN

client = commands.Bot(command_prefix=";")

logging.basicConfig(level="INFO")
logger = logging.getLogger("main.py")

extensions = [
    "events.on_error",
    "events.on_member_join",
    "events.on_message",
    "events.on_ready",
    "commands.about",
    "commands.dontasktoask",
    "commands.ping",
    "commands.say",
    "commands.tutorban",
    "commands.tutorunban",
    "commands.close",
    "commands.assign",
    "commands.unassign",
]

for extension in extensions:
    try:
        client.load_extension(extension)
    except Exception:
        logger.error(
            f"Failed to load {extension} with error:\n{traceback.format_exc()}"
        )

client.run(TOKEN)
