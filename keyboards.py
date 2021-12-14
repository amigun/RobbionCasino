from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import messages

main_menu__kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu__kb.add(KeyboardButton(messages.buttons['play']),
                  KeyboardButton(messages.buttons['profile']))

get = {
    'main_menu': main_menu__kb,
}