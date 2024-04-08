"""
If you are deploying it locally then follow following steps:
Remove all the thing after = sign except in category part.
Pass the values directly i.e. without using quotaion where int is written.
Pass the value in C like "First Second Third" make sure you seprate them using space.
"""


from os import getenv

API_ID = int(getenv("API_ID", 24269862))
API_HASH = getenv("API_HASH", 5b1a646f8c8ed40f15af84c9b2dfa9e8)
BOT_TOKEN = getenv("BOT_TOKEN", 6977508784:AAHIPQpM_bQ6YVJGT0HY4llO8aP3Opc67Nw)
DB_URI = getenv("DB_URI", mongodb+srv://nox:nox@nox.0erqdpv.mongodb.net/?retryWrites=true&w=majority
)
DB_NAME = getenv("DB_NAME", referbot)
OWNER = int(getenv("OWNER_ID", 5154912723))
DEV = int(getenv("DEV", 5154912723)
SUDO = list({int(i) for i in getenv("SUDO").split()})
C = getenv("CATEGORY").split(None) # Don't remove this line
x = []
for i in C:
    x.append(i.strip().lower())
COIN_NAME = str(getenv("COIN_NAME", REFLEX))
COIN_EMOJI = getenv("COIN_EMOJI")
NUMBER_MESSAGE = int(getenv("NUMBER_MESSAGE"))
COIN_MESSAGE = int(getenv("COIN_MESSAGE"))
CATEGORY = x
WITHIN = int(getenv("WITHIN"))
LIMIT = int(getenv("LIMIT"))
TIME = getenv("TIME")
unit = str(TIME[-1]).lower()
time_num = int(TIME[:-1])
AMOUNT = int(getenv("AMOUNT", 5))
CHAT_ID = int(getenv("CHAT_ID" -1002052189895))
PREMIUM_CHANNEL = int(getenv("PREMIUM_CHANNEL"))
PREMIUM_COST = int(getenv("PREMIUM_COST", 50))
