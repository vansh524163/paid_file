import sys
import asyncio
import logging
import traceback
from aiohttp import web
from pyrogram import Client, idle
from FileStream.config import Telegram, Server
from FileStream.bot import FileStream
from FileStream.server import web_server
from FileStream.bot.clients import initialize_clients

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Capture all levels of logs
    datefmt="%d/%m/%Y %H:%M:%S",
    format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(stream=sys.stdout),  # Outputs to console
        logging.handlers.RotatingFileHandler(
            "streambot.log", 
            mode="a", 
            maxBytes=104857600, 
            backupCount=2, 
            encoding="utf-8"
        )  # Outputs to a file with rotation
    ],
)

# Set specific logging levels for libraries
logging.getLogger("aiohttp").setLevel(logging.DEBUG)
logging.getLogger("pyrogram").setLevel(logging.DEBUG)
logging.getLogger("aiohttp.web").setLevel(logging.DEBUG)

# Create a logger instance
logger = logging.getLogger(__name__)

server = web.AppRunner(web_server())
loop = asyncio.get_event_loop()

async def start_services():
    try:
        logger.info("Starting services...")
        if Telegram.SECONDARY:
            logger.info("Starting as Secondary Server")
        else:
            logger.info("Starting as Primary Server")
        
        logger.info("Initializing Telegram Bot")
        await FileStream.start()
        bot_info = await FileStream.get_me()
        FileStream.id = bot_info.id
        FileStream.username = bot_info.username
        FileStream.fname = bot_info.first_name
        logger.info(f"Bot info - ID: {bot_info.id}, Username: {bot_info.username}, First Name: {bot_info.first_name}")

        logger.info("Initializing Clients")
        await initialize_clients()
        
        logger.info("Initializing Web Server")
        await server.setup()
        await web.TCPSite(server, Server.BIND_ADDRESS, Server.PORT).start()

        logger.info(f"Service Started. URL: {Server.URL}")
        await idle()
    except Exception as e:
        logger.error("Error starting services", exc_info=True)

async def cleanup():
    try:
        await server.cleanup()
        await FileStream.stop()
        logger.info("Cleanup completed.")
    except Exception as e:
        logger.error("Error during cleanup", exc_info=True)

if __name__ == "__main__":
    try:
        loop.run_until_complete(start_services())
    except KeyboardInterrupt:
        logger.info("Service interrupted by user.")
    except Exception as e:
        logger.error("Unhandled exception occurred", exc_info=True)
    finally:
        loop.run_until_complete(cleanup())
        loop.stop()
        logger.info("Stopped services.")
