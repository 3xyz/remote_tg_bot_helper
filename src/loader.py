from aiogram import Bot
from aiogram import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.config import BOT_TOKEN, ADMIN_IDS

storage = MemoryStorage()

bot = Bot(token=BOT_TOKEN, parse_mode='HTML')  # , server=local_server
dp = Dispatcher(bot, storage=storage)
# dp.register_message_handler(IDFilter=ADMIN_IDS)
