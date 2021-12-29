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


async def select_mode_duo(call: types.CallbackQuery):
    await fsm.MainStates.select_duo_game.set()

    await call.message.edit_text(messages.get['select_game'], reply_markup=kb.get['select_duo_game'])


async def select_duo_game(call: types.CallbackQuery):
    if call.data == 'back':
        await fsm.MainStates.select_mode.set()

        await call.message.edit_text(text=messages.get['select_mode'], reply_markup=kb.get['select_mode'])


async def menu(msg: types.Message, state: FSMContext):
    if msg.text == messages.buttons['profile']:
        await msg.answer(messages.get['profile'].format(*db_queries.user_info(msg.from_user.id)))
    elif msg.text == messages.buttons['play']:
        await fsm.MainStates.select_mode.set()

        await msg.answer(messages.get['select_mode'], reply_markup=kb.get['select_mode'])


def register_handler(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(menu, state='*')
    dp.register_callback_query_handler(select_mode_duo, text='duo_mode', state=fsm.MainStates.select_mode)
    dp.register_callback_query_handler(select_duo_game, lambda callback_query: True, state=fsm.MainStates.select_duo_game)