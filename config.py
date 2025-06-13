import re
import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required credentials
API_ID = 22565342
API_HASH = "75e035926f72f2f4155a6f5f6e64be03"
BOT_TOKEN = "7201420162:AAGxAlHuNHtf_OZKKBwrAZhhD6vX6PB4HgM"
MONGO_DB_URI = "mongodb+srv://mikey:mikey@cluster0.zv6knh9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
OWNER_ID = 7926944005
LOG_GROUP_ID = -1002777786186

# Optional / deployment-related
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY")

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://t.me/infinitygx_bot_support")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = os.getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/dark_x_knight_musiczz_support")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/dark_knight_support")
PRIVACY_LINK = os.getenv("PRIVACY_LINK", "https://telegra.ph/Privacy-Policy-for-AviaxMusic-08-14")

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 10000))
DURATION_LIMIT = DURATION_LIMIT_MIN * 60

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", None)
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

STRING1 = "BQFYUd4AaBQ-7rxbKMguDsyH8oJPUtsDN4JBK4J-P09mTvQkHm24IsRuD3VtdQi1nbxvR97mcLHog1Ke9s6dKIYskILAyeaNzfr7CayVeDm_hiY0XKz9Ge7BR8A4KXBFdpUy_9KA7t0yDheKWcdJOM-ArBjs40uUUIjyPd0tntz3tWArfLmttWkuUNI2LGmTn_EjZjBH_XRopuZNVsesynDa7C5z8a-5V_Z87OKlzkoQL8u5Tw34EYMA_0eBsdjuEs5-rU2gz80eDSdIf9e0Pf7vWxy8tPxRjNe6DROsj5-m-CEys1SIoF_Uaw0jCZo8lZRRFk_ezLpnp2zclT0dk3iCxJDPeQAAAAHjZt-vAA"
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = os.getenv("START_IMG_URL", "https://graph.org/file/998d2db9c003c1625178c-21d9359fc3b61485f7.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://graph.org//file/389a372e8ae039320ca6c.png")
PLAYLIST_IMG_URL = "https://graph.org//file/3dfcffd0c218ead96b102.png"
STATS_IMG_URL = "https://graph.org//file/99a8a9c13bb01f9ac7d98.png"
TELEGRAM_AUDIO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
TELEGRAM_VIDEO_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://graph.org//file/2f7debf856695e0ef0607.png"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"

# Time converter
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

# Validate links
if SUPPORT_CHANNEL and not re.match("(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. It must start with https://")

if SUPPORT_GROUP and not re.match("(?:http|https)://", SUPPORT_GROUP):
    raise SystemExit("[ERROR] - Your SUPPORT_GROUP url is wrong. It must start with https://")