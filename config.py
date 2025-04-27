"""
from os import getenv


API_ID = int(getenv("API_ID", "22923037"))
API_HASH = getenv("API_HASH", "dfb3666878b3851460a58461c5a50f5b")
BOT_TOKEN = getenv("BOT_TOKEN", "7751391316:AAEl3Sjwt5PHxZw9QtffalbXHVUB0hmkazA")
OWNER_ID = int(getenv("OWNER_ID", "6554343173"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7081036509 7491167754 6554343173").split()))
MONGO_URL = getenv("MONGO_DB", "mongodb+srv://vikassonawale0:JWyQFas7vlG1bkaL@cluster0.beermge.mongodb.net/?retryWrites=true&w=majority")

CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002574084986"))
PREMIUM_LOGS = int(getenv("PREMIUM_LOGS", "-1002261145026"))

"""
#




# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("BOT_USERNAME")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS"))

