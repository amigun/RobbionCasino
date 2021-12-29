from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

import db_queries
import messages
import keyboards as kb
import fsm


async def start(msg: types.Message, state: FSMContext):
    await msg.answer(messages.get['greeting'], reply_markup=kb.get['main_menu'])

    db_queries.user_register(msg.from_user.id)

    try:
        if msg.get_args() and isinstance(int(msg.get_args()), int):
            db_queries.set_owner(msg.from_user.id, msg.get_args())
    except ValueError:
        pass

    await fsm.MainStates.main_menu.set()


async def menu(msg: types.Message, state: FSMContext):
    if msg.text == messages.buttons['profile']:
        await msg.answer(messages.get['profile'].format(*db_queries.user_info(msg.from_user.id)))
    elif msg.text == messages.buttons['play']:
        await msg.answer(messages.get['select_mode'], reply_markup=kb.get['select_mode'])


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(menu, state=fsm.MainStates.main_menu)