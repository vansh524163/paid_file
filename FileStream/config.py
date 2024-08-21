import logging
from os import environ as env
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.DEBUG,  # Set to DEBUG to capture all logs
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.StreamHandler(),  # Outputs to console
                        logging.FileHandler("app.log")  # Outputs to a file
                    ])

logger = logging.getLogger(__name__)

# Define classes with enhanced error handling
class Telegram:
    try:
        API_ID = int(env.get("API_ID", '21956488'))
        API_HASH = str(env.get("API_HASH", '812529f879f06436925c7d62eb49f5d1'))
        BOT_TOKEN = str(env.get("BOT_TOKEN", '7045827644:AAF0Gmh07-D6Qaj64EG-GyP6-HniviX2gdo'))
        OWNER_ID = int(env.get('OWNER_ID', '2020224264'))
        WORKERS = int(env.get("WORKERS", "6"))  # 6 workers = 6 commands at once
        DATABASE_URL = str(env.get('DATABASE_URL', 'mongodb+srv://kavijoy952:8qOZ2k2VfeFVcWc1@cluster0.enxbb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'))
        UPDATES_CHANNEL = str(env.get('UPDATES_CHANNEL', "update_info4_bot"))
        SESSION_NAME = str(env.get('SESSION_NAME', 'FileStream'))
        FORCE_SUB_ID = env.get('FORCE_SUB_ID', None)
        FORCE_SUB = str(env.get('FORCE_UPDATES_CHANNEL', "False")).lower() in ("1", "true", "t", "yes", "y")
        SLEEP_THRESHOLD = int(env.get("SLEEP_THRESHOLD", "60"))
        FILE_PIC = env.get('FILE_PIC', "https://graph.org/file/5bb9935be0229adf98b73.jpg")
        START_PIC = env.get('START_PIC', "https://graph.org/file/290af25276fa34fa8f0aa.jpg")
        VERIFY_PIC = env.get('VERIFY_PIC', "https://graph.org/file/736e21cc0efa4d8c2a0e4.jpg")
        MULTI_CLIENT = False
        FLOG_CHANNEL = int(env.get("FLOG_CHANNEL", -1002065793080))   # Logs channel for file logs
        ULOG_CHANNEL = int(env.get("ULOG_CHANNEL", -1002065793080))   # Logs channel for user logs
        MODE = str(env.get("MODE", "primary")).lower()
        SECONDARY = MODE == "secondary"
        AUTH_USERS = list(set(int(x) for x in str(env.get("AUTH_USERS", "")).split() if x.isdigit()))
        STREAM_URL = env.get("STREAM_URL", "https://ddbots.blogspot.com/p/stream.html")
        DOWNLOAD_URL = env.get("DOWNLOAD", "https://ddbots.blogspot.com/p/download.html")
        FILES_URL = env.get("FILES_URL", "https://ddbots.blogspot.com/p/files.html")
    except Exception as e:
        logger.error("Error initializing Telegram settings", exc_info=True)

class Server:
    try:
        PORT = int(env.get("PORT", 8080))
        BIND_ADDRESS = str(env.get("BIND_ADDRESS", "0.0.0.0"))
        PING_INTERVAL = int(env.get("PING_INTERVAL", "1200"))
        HAS_SSL = str(env.get("HAS_SSL", "0").lower()) in ("1", "true", "t", "yes", "y")
        NO_PORT = str(env.get("NO_PORT", "0").lower()) in ("1", "true", "t", "yes", "y")
        FQDN = str(env.get("FQDN", BIND_ADDRESS))
        URL = f"http{'s' if HAS_SSL else ''}://{FQDN}{'' if NO_PORT else f':{PORT}'}"
    except Exception as e:
        logger.error("Error initializing Server settings", exc_info=True)
