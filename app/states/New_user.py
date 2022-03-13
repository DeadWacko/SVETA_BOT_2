from aiogram.dispatcher.filters.state import StatesGroup, State


class NewUser(StatesGroup):
    #Добавление нового преподавателя
    choice_team = State()
    add_fullname = State()
    add_ID = State()
    check_user_validation = State()
    on = State()
    #Состояния связанные с меню:
    menu_1 = State()
    menu_1_1 = State()



class menu_1_1(StatesGroup):
    get_back_link = State()

    change_format = State()
    check_correct_format = State()
    reason_return = State()
    twelve_hour = State()

