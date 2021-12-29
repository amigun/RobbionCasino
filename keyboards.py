from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

import messages

main_menu__kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu__kb.add(KeyboardButton(messages.buttons['play']),
                  KeyboardButton(messages.buttons['profile']))

select_mode__kb = InlineKeyboardMarkup()
select_mode__kb.add(InlineKeyboardButton(text=messages.buttons['solo'], callback_data='solo_mode'),
                    InlineKeyboardButton(text=messages.buttons['duo'], callback_data='duo_mode'))

select_duo_game__kb = InlineKeyboardMarkup()
for game in list(messages.buttons['duo_games']):
    select_duo_game__kb.add(InlineKeyboardButton(text=messages.buttons['duo_games'][game], callback_data=game))
select_duo_game__kb.add(InlineKeyboardButton(text=messages.buttons['back'], callback_data='back'))

get = {
    'main_menu': main_menu__kb,
    'select_mode': select_mode__kb,
    'select_duo_game': select_duo_game__kb,
}