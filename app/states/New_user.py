from aiogram.dispatcher.filters.state import StatesGroup, State


class NewUser(StatesGroup):
    #Добавление нового преподавателя
    choice_team = State()
    add_fullname = State()
    add_ID = State()
    check_user_validation = State()

    #Состояния связанные с меню:
    menu_1 = State()
    menu_1_1 = State()



class menu_1_1(StatesGroup):
    change_format = State()
    reason_return = State()
    twelve_hour = State()

