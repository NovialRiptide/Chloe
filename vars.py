import mysql.connector

MEMBERS_WITH_PERMS = [182288858782629888, 389932655111831562]

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

QUOTES = [
    "Never gonna give you up, never gonna let you down.",
    "May the Force be with you.",
    "I\'ll be back.",
    "It\'s alive! It\'s alive!",
    "Houston, we have a problem.",
    "I\'m king of the world!",
    "There\'s no time to explain!",
    "Please don't make the super suit green... or animated!",
    "Just because something works, doesn\'t mean it can\'t be improved.",
    "It\'s an imperfect world but it\'s the only one we got.",
    "My precious.",
    "E.T. phone home.",
    "Just keep swimming.",
    "Here\'s Johnny!",
    "To infinity and beyond!",
    "There\'s a snake in my boot!",
    "Toto, I've a feeling we\'re not in Kansas anymore.",
    "Choice is an illusion, play monopoly",
    "Freeze! It's the anime police!",
    "It doesn\'t matter if she\'s imaginary, the thiccness exists in our hearts."
]

PING_REE = [
    695502565668028468, # professional
    389932655111831562, # shauna 
    287159796988248064, # lush
    691604047064596480, # brooke
    583667262460919818, # lsd
    199586464256884737  # joren
]

MAIN_TUTOR_ROLE = 630183885623525424
TUTOR_ROLES = {
    "MATH": 724158494072111175,
    "SCIENCE": 724158499524968488,
    "HISTORY": 724159960627281931,
    "ENGLISH": 724158482286379092
}

def tsc_ongoing_session(user):
    return f"__**How to ask for help:**__\n:question: | Post your question! *Don't just say \"help\".*\n:eye: | Add any images, sources, or texts that will help the tutors.\n:school_satchel: | Inform the tutor of what level the question is. *(e.g. trigonometry, calculus BC, stoichiometry)*\n\n**Once the above is complete, ping the respective tutor role once!**\n\n{user}"

MYSQL_HOST = "ec2-18-233-32-61.compute-1.amazonaws.com"
MYSQL_USER = "rkaqpfzulzeuyc"
MYSQL_PASS = "7746edab4fb7cb9e446684aa950e4c46e9d1bcb23c8a4845d5f6638cecfc792c"
"""
mydb = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASS
)
print(mydb)
"""