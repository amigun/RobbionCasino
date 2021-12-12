from aiogram import types, Dispatcher

import db_queries
import messages
import keyboards as kb


async def start(msg: types.Message):
    await msg.answer(messages.get['greeting'], reply_markup=kb.get['main_menu'])

    db_queries.user_register(msg.from_user.id)

    try:
        if msg.get_args() and isinstance(int(msg.get_args()), int):
            print(msg.get_args())
            db_queries.set_owner(msg.from_user.id, msg.get_args())
    except ValueError:
        pass


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])