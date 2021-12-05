from aiogram import types, Dispatcher

import messages
import keyboards as kb


async def start(message: types.Message):
    await message.answer(messages.get['greeting'], reply_markup=kb.get['main_menu'])


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])