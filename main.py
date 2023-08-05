#!/usr/bin/env python3
import sys

from aiogram import executor
from loguru import logger

from src import handler
from src.config import ADMIN_IDS
from src.config import LOG
from src.config import LOG_JSON
from src.loader import bot
from src.loader import dp

__all__ = [
    "handler",
]


# TEST: Eating first line


async def on_startup(dp):
    loguru_setup()
    for admin_id in ADMIN_IDS:
        await bot.send_message(admin_id, "Running")


async def on_shutdown(dp):
    await bot.close()


def loguru_setup():
    # logger.remove()
    default_format = "[<level>{level}</level>] {message}"
    logger.add(sys.stderr, level="INFO", format=default_format, colorize=True)
    debug_format = "[<level>{level}</level>] {message} [<cyan>{name}:{function}:{line}</cyan>] [<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green>]"
    logger.add(LOG, level="DEBUG", format=debug_format, colorize=True, rotation="10 MB")
    logger.add(LOG_JSON, level="DEBUG", serialize=True, rotation="100 MB")


if __name__ == "__main__":
    try:
        executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
