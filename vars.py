MEMBERS_WITH_PERMS = [182288858782629888, 389932655111831562]

MEMBERS_BLACKLISTED = [
    234619517878272000, # callum
    563151366378225694, # garlic
    658632975482617889, # joe
]

VALID_CHANNEL_JSON_KEYS = {
    "logging": "int",
    "sessions": "list",
    "join_leave": "int",
    "auto_announce": "int"
}

VALID_SESSION_CATEGORIES = [
    "dormant",
    "available",
    "occupied"
]

BLACKLISTED_WORDS = [
    "nigger",
    "nigga",
    "nibba",
    "niga",
    "redskin",
    "red skin"
]

POSITIVE_WORDS = [

]

NEGATIVE_WORDS = [
    "stupid"
]

PHRASES = [
    ["ur", "gay"],
    ["chloe", "is", NEGATIVE_WORDS]
]

MAX_NUMBER_OF_AVAILABLE_SESSIONS = 2

FOOTER = "Bot Developed by Novial // Andrew Hong"

INVALID_DATABASE_ERROR = f"It seems like you are not in the Chloë database. Do ``!setup`` to continue."

MISSING_ARGUMENTS_ERROR = "You are missing some arguments..."
TOO_MANY_ARGUMENTS_ERROR = "You have too many arguments!"
USER_INPUT_ERROR = "You have inputted your arguments wrong!"
NO_PERMISSION_ERROR = "You do not have permission to do this..."
BOT_NO_PERMISSION_ERROR = "I do not have permission to do this..."
UNKNOWN_COMMAND_ERROR = "I have never heard of this command before."

FAKE_ERROR = "An error has occurred. Please try again later."

def tsc_ongoing_session(user):
    return f"__**How to ask for help:**__\n:question: | Post your question! *Don't just say \"help\".*\n:eye: | Add any images, sources, or texts that will help the tutors.\n:school_satchel: | Inform the tutor of what level the question is. *(e.g. trigonometry, calculus BC, stoichiometry)*\n\n**Once the above is complete, ping the respective tutor role once!**\n\n{user}"
