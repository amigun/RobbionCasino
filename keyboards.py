from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu__kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu__kb.add(KeyboardButton('🎮 Играть'),
                  KeyboardButton('👨‍💼 Профиль'))

get = {
    'main_menu': main_menu__kb,
}