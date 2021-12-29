from aiogram.dispatcher.filters.state import State, StatesGroup


class MainStates(StatesGroup):
    main_menu = State()
    select_mode = State()
    select_duo_game = State()