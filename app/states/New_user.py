from aiogram.dispatcher.filters.state import StatesGroup, State


class NewUser(StatesGroup):
    # Добавление нового преподавателя
    choice_team = State()
    add_fullname = State()
    add_ID = State()
    check_user_validation = State()
    on = State()
    # Состояния связанные с меню:
    menu_1 = State()
    menu_1_1 = State()


class menu_1_1(StatesGroup):
    get_back_link: State = State()
    get_back_link_2: State = State()
    get_back_link_3: State = State()
    get_back_link_4: State = State()
    get_back_link_5: State = State()
    get_back_link_6: State = State()
    get_back_link_7: State = State()
    get_back_link_8: State = State()
    get_back_link_9: State = State()

    yes_no_3: State = State()
    concellation: State = State()
    old_data: State = State()
    new_data: State = State()
    check_correct_cancellation: State = State()
    check_correct_return: State = State()
    change_format: State = State()
    couse_return: State = State()
    check_correct_format: State = State()
    reason_return: State = State()
    twelve_hour: State = State()
    question_cash: State = State()
    check_question_cash: State = State()
    new_course: State = State()
    check_teacher_change: State = State()
    check_shedule: State = State()
    get_new_date: State = State()
    get_new_time: State = State()
    check_question_change_1: State = State()
    check_question_change_2: State = State()
    get_number_missed_classes: State = State()
    correct_number_missed_classes_1: State = State()
    check_reason_for_missing: State = State()
    correct_cause_missed_classes_1: State = State()
    get_reason_for_missing: State = State()
    get_in_touch: State = State()
