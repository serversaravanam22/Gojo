import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "7891414677:AAHqmQ_DifBrHvboH6VkL9TVqeu_BCEgfsg")
API_ID = int(os.environ.get("API_ID", "14307449"))
API_HASH = os.environ.get("API_HASH", "51581b3f5f95c2c7f97efa2608d8e4f1")


OWNER_ID = int(os.environ.get("OWNER_ID", "7035627523"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://boyrokey00:db_rajan123@cluster0.4fhuu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Pream3")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002253632172"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002191966684"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002161437490"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8000")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6848088376]
    for x in (os.environ.get("ADMINS", "6693549185").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "Hello {mention}\n\nI Can Store Private Files In Specified Channel And Other Users Can Access It From Special Link.")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Aɴɪᴍᴇ Fɪʟᴇs\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟs\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a href=https://t.me/Tamil_Anime_Files/893>Tᴜᴛᴏʀɪᴀʟ</a></b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6848088376)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
