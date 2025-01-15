import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8186748271:AAFDh4hdtHXSYYAPk6jBikC6eMScKK60MAQ")
API_ID = int(os.environ.get("API_ID", "20902603"))
API_HASH = os.environ.get("API_HASH", "79e5caa103a9e9fb0183390b4800845d")


OWNER_ID = int(os.environ.get("OWNER_ID", "6283322330"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://ganeshganesh177:17032009@sasukeuchiha.k21bh.mongodb.net/?retryWrites=true&w=majority&appName=Sasukeuchiha")
DB_NAME = os.environ.get("DB_NAME", "Sasukeuchiha")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002448160632"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002262460059"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002399764589"))


FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6283322330]
    for x in (os.environ.get("ADMINS", "6283322330").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\nI cᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇs ɪɴ sᴘᴇcɪꜰɪc cʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs cᴀɴ ᴀccᴇss ɪᴛ ꜰʀᴏᴍ sᴘᴇcɪᴀʟ ʟɪɴᴋs")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hᴇʟʟᴏ {mention}\n\n<b>Yᴏᴜ Nᴇᴇᴅ Tᴏ Jᴏɪɴ Iɴ Mʏ Cʜᴀɴɴᴇʟs Tᴏ Gᴇᴛ Aɴɪᴍᴇ Fɪʟᴇs\n\nKɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ Cʜᴀɴɴᴇʟs\n\nIғ ʏᴏᴜ ᴅᴏɴ'ᴛ ᴋɴᴏᴡ ʜᴏᴡ ᴛᴏ ɢᴇᴛ ғɪʟᴇ ᴄʜᴇᴄᴋ <a href=https://t.me/Tamil_Anime_Files/893>Tᴜᴛᴏʀɪᴀʟ</a></b>")





ADMINS.append(OWNER_ID)
ADMINS.append(6283322330)

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
