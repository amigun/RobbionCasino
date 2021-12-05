import os

from dotenv import load_dotenv

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import keyboards as kb
import messages

load_dotenv('.env')

bot = Bot(token=os.environ.get('TG_TOKEN'))
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(messages.get['greeting'], reply_markup=kb.get['main_menu'])


if __name__ == '__main__':
    executor.start_polling(dp)