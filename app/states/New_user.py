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
    get_back_link_2 = State()
    get_back_link_3 = State()
    get_back_link_4 = State()

    yes_no_3 = State()
    concellation = State()
    old_data = State()
    new_data = State()
    check_correct_cancellation = State()
    check_correct_return = State()
    change_format = State()
    couse_return = State()
    check_correct_format = State()
    reason_return = State()
    twelve_hour = State()
    question_cash = State()
    check_question_cash = State()

