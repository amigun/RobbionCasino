from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import messages

main_menu__kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu__kb.add(KeyboardButton(messages.buttons['play']),
                  KeyboardButton(messages.buttons['profile']))

select_mode__kb = InlineKeyboardMarkup()
select_mode__kb.add(InlineKeyboardButton(text=messages.buttons['solo'], callback_data='solo_mode'),
                    InlineKeyboardButton(text=messages.buttons['duo'], callback_data='duo_mode'))

get = {
    'main_menu': main_menu__kb,
    'select_mode': select_mode__kb,
}