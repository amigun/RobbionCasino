import os

from dotenv import load_dotenv
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

import handlers

load_dotenv('.env')

bot = Bot(token=os.environ.get('TG_TOKEN'))
dp = Dispatcher(bot, storage=MemoryStorage())

handlers.main.register_handler(dp)

if __name__ == '__main__':
    executor.start_polling(dp)