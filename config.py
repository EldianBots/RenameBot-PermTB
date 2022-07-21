import os

class Config(object):

    # get a token from @BotFather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5550235697:AAFsLeT10_jukn7CjDCOKbOHHQEkbJ9o2UU")

    # The Telegram API things
    APP_ID = int(os.environ.get("APP_ID", 9565646))
    API_HASH = os.environ.get("API_HASH", 8bef4f16c95732f213be784cc6f3b107)
    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "5058430095").split())

    # Ban Unwanted Members..
    BANNED_USERS = []

    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

    # chunk size that should be used with requests
    CHUNK_SIZE = 128

    # Database url
    DB_URI = os.environ.get("DATABASE_URL", "postgres://ofclivhn:dUAYurXs2SS3agtwgDCw_myUKipX8g5w@jelani.db.elephantsql.com/ofclivhn")

