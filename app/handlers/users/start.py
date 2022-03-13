import random
import re
from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.types import callback_query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.util import NoneType
from app.db_api.models import User

from app.keyboards.inline.first_choise import team_keyboard, yesno_keyboard_markup, menu_1, menu_1_1_keyboard

from app.states import NewUser, menu_1_1


async def start(message: types.Message, db: AsyncSession):
    """Старт. В зависимости от того Новый/старый пользователь перед нами отвечаем ему. Если новый - добавляем. Если старый-кидаем ему меню"""
    data = await db.get(User, message.from_user.id)  # Грузим все данные по этому пользователю из БД
    if type(data) != NoneType:  # Если пользователь есть - то грузим его сразу в меню. Иначе грузим его в ф-ю добавления
        await message.answer(f"Так,ты уже есть. Лови сразу меню:3")
        # Кидаем его в состояние основного меню и отправляем клавиатуру
        # await NewUser.state_new_user.set()
        await NewUser.menu_1.set()

    else:
        await message.answer(f"Привет, смотрю ты тут в первый раз, давай впишем всю основную ирнформацию по тебе",
                             reply_markup=team_keyboard)
        await NewUser.choice_team.set()  # Кидаем его в состояние, где он добавит всю необходимую информацию о себе |||+|||


########################################################################################################################
async def answer_team(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    await callback.message.edit_text(f"ты нажал {callback.data}")
    async with state.proxy() as data:
        data["team_name"] = callback.data
    await NewUser.add_fullname.set()  # туть мы бросаем в следующее состояние
    await callback.message.answer("Введи свое ФИО")


async def add_fullname(message: types.Message, state: FSMContext, db: AsyncSession):
    async with state.proxy() as data:
        data["full_name"] = message.text
    await message.answer("ВВЕДИ СВОЙ ID")
    await NewUser.add_ID.set()  # туть мы бросаем в следующее состояние


async def add_kodland_ID(message: types.Message, state: FSMContext, db: AsyncSession):
    user_kodland_id = message.text
    async with state.proxy() as data:
        await message.answer(
            f"Давай проверим твои данные:\n\t\t Номер команды: {data['team_name']} \n\t\t Твое ФИО: {data['full_name']}\n\t\t Твой ID: {user_kodland_id}\n Все верно??",
            reply_markup=yesno_keyboard_markup)
        await NewUser.check_user_validation.set()


# Проверяем все ли правильно ввел пользователь. если да- кидаем основное меню. если нет - кидаем в начало
async def check_user_validation(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    if callback.data == "yes":
        await callback.message.edit_text("Прекрасно, лови меню✅", reply_markup=menu_1)
        await NewUser.menu_1.set()
        # ВЫГРУЖАЕМ ВСЕ ДАННЫЕ В БД
    else:
        await callback.message.edit_text("Ничего страшного, начнем заново", reply_markup=team_keyboard)
        await NewUser.choice_team.set()


# Ветка вопросов связанных с учениками
async def first_menu(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    await callback.message.edit_text("Вопросы связанные с учениками", reply_markup=menu_1_1_keyboard)


########################################################################################################################
# Смена формата обучения
# просим ввести ссылочку на ученика
async def send_message_with_link(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите ссылку на ученика:")
    await menu_1_1.get_back_link.set()


# хватаем ссылочку на ученика
async def get_link(message: types.Message, state: FSMContext, db: AsyncSession):
    async with state.proxy() as data:
        data["link"] = message.text
    await message.answer("Введите новый формат обучения")
    await menu_1_1.change_format.set()


# Просим ввести новый формат обучения ученика
async def get_new_format(message: types.Message, state: FSMContext, db: AsyncSession):
    new_format = message.text
    async with state.proxy() as data:
        await message.answer(
            f"Давай проверим твои данные:\n\t\t ссылка на ученика: {data['link']} \n\t\t Новый формат: {new_format}\n Все верно??",
            reply_markup=yesno_keyboard_markup)
        await menu_1_1.check_correct_format.set()


async def check_correct_group_format(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    if callback.data == "yes":
        await callback.message.edit_text("Прекрасно, лови меню✅", reply_markup=menu_1)
        # await NewUser.menu_1.set()
        # ВЫГРУЖАЕМ ВСЕ ДАННЫЕ В ТАБЛИЦУ
    else:
        await callback.message.edit_text("Ничего страшного, начнем заново", reply_markup=menu_1_1_keyboard)


########################################################################################################################
# Хочет бросить обучение /Сделать возврат


# просим ввести ссылочку на ученика +
async def send_message_with_link_2(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите ссылку на ученика:")
    await menu_1_1.get_back_link_2.set()


# хватаем ссылочку на ученика +
async def get_link_2(message: types.Message, state: FSMContext, db: AsyncSession):
    async with state.proxy() as data:
        data["link"] = message.text
    await message.answer("Причина возврата:")
    await menu_1_1.couse_return.set()


# Просим ввести причину возврата+
async def get_cause_return(message: types.Message, state: FSMContext, db: AsyncSession):
    new_format = message.text
    async with state.proxy() as data:
        await message.answer(
            f"Давай проверим твои данные:\n\t\t ссылка на ученика: {data['link']} \n\t\t Причина возврата: {new_format}\n Все верно??",
            reply_markup=yesno_keyboard_markup)
        await menu_1_1.check_correct_return.set()


async def check_correct_return(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    if callback.data == "yes":
        await callback.message.edit_text("Прекрасно, лови меню✅", reply_markup=menu_1)
        # await NewUser.menu_1.set()
        # ВЫГРУЖАЕМ ВСЕ ДАННЫЕ В ТАБЛИЦУ
    else:
        await callback.message.edit_text("Ничего страшного, начнем заново", reply_markup=menu_1_1_keyboard)


########################################################################################################################
# Отмена/перенос


# просим ввести ссылочку на ученика +
async def send_message_with_link_3(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите ссылку на ученика:")
    await menu_1_1.get_back_link_3.set()


# хватаем ссылочку на ученика +
async def get_link_3(message: types.Message, state: FSMContext, db: AsyncSession):
    async with state.proxy() as data:
        data["link"] = message.text
    await message.answer("Запрос поступил более чем за 12 часов?", reply_markup=yesno_keyboard_markup)
    await menu_1_1.yes_no_3.set()


async def check_twelve_hours(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    if callback.data == "yes":
        async with state.proxy() as data:
            data["twelve_house"] = "Да"
        await callback.message.edit_text("Причина отмены/переноса")

    else:
        async with state.proxy() as data:
            data["twelve_house"] = "Нет"
        await callback.message.edit_text("Причина отмены/переноса")
    # состояние для отмены/переноса
    await menu_1_1.concellation.set()


# Просим ввести причину переноса/отмены
async def get_cause_cancellation(message: types.Message, state: FSMContext, db: AsyncSession):
    new_format = message.text
    async with state.proxy() as data:
        data["cause_cancellation"] = new_format

    await message.answer("Введите первоначальную дату")
    # состояние для ввода первоначальной даты
    await menu_1_1.old_data.set()


# Просим ввести первоначальную дату
async def get_old_data(message: types.Message, state: FSMContext, db: AsyncSession):
    new_format = message.text
    async with state.proxy() as data:
        data["old_data"] = new_format
    await message.answer("Введите новую дату")
    await menu_1_1.new_data.set()
    # состояние для ввода новой даты


# Просим ввести новую дату
async def get_new_data(message: types.Message, state: FSMContext, db: AsyncSession):
    new_data = message.text
    async with state.proxy() as data:
        await message.answer(
            f"Давай проверим твои данные:\n\t\t ссылка на ученика: {data['link']} \n\t\t Запрос поступил за 12ч?:"
            f" {data['twelve_house']} \n\t\t Причина отмены/переноса?: {data['cause_cancellation']}\n\t\t"
            f" Первоначальная дата занятия: {data['old_data']}\n\t\t Новая дата занятия: {new_data}\n"
            f" Все верно??",
            reply_markup=yesno_keyboard_markup)
        await menu_1_1.check_correct_cancellation.set()


async def check_correct_cancellation(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    if callback.data == "yes":
        await callback.message.edit_text("Прекрасно, лови меню✅", reply_markup=menu_1)
        # await NewUser.menu_1.set()
        # ВЫГРУЖАЕМ ВСЕ ДАННЫЕ В ТАБЛИЦУ
    else:
        await callback.message.edit_text("Ничего страшного, начнем заново", reply_markup=menu_1_1_keyboard)




########################################################################################################################
                                    # Оплата учеников
# просим ввести ссылочку на ученика +
async def send_message_with_link_4(callback: types.CallbackQuery):
    await callback.message.edit_text("Введите ссылку на ученика:")
    await menu_1_1.get_back_link_4.set()


# хватаем ссылочку на ученика +
async def get_link_4(message: types.Message, state: FSMContext, db: AsyncSession):
    async with state.proxy() as data:
        data["link"] = message.text
    await message.answer("Какой вопрос возник, касательно оплаты?")
    await menu_1_1.question_cash.set()


# Просим ввести вопрос  касательно оплаты?
async def get_question_cash(message: types.Message, state: FSMContext, db: AsyncSession):
    question_cash = message.text
    async with state.proxy() as data:
        await message.answer(
            f"Давай проверим твои данные:\n\t\t ссылка на ученика: {data['link']} \n\t\t Проблема возникшая по оплате: {question_cash}\n Все верно??",
            reply_markup=yesno_keyboard_markup)
        await menu_1_1.check_question_cash.set()


async def check_correct_question_cash(callback: types.CallbackQuery, state: FSMContext, db: AsyncSession):
    if callback.data == "yes":
        await callback.message.edit_text("Прекрасно, лови меню✅", reply_markup=menu_1)
        # await NewUser.menu_1.set()
        # ВЫГРУЖАЕМ ВСЕ ДАННЫЕ В ТАБЛИЦУ
    else:
        await callback.message.edit_text("Ничего страшного, начнем зановоggeg", reply_markup=menu_1)
    state.finish()













async def exit(callback: types.CallbackQuery):
    await callback.message.edit_text("Главное меню", reply_markup=menu_1)


########################################################################################################################
def register_start(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart())
    dp.register_callback_query_handler(answer_team, state=NewUser.choice_team)
    dp.register_message_handler(add_fullname, state=NewUser.add_fullname)
    dp.register_message_handler(add_kodland_ID, state=NewUser.add_ID)
    dp.register_callback_query_handler(check_user_validation, state=NewUser.check_user_validation)
    dp.register_callback_query_handler(first_menu, text="questions_about_students", state="*")
    dp.register_callback_query_handler(exit, text="exit")

    # Смена формата обучения
    dp.register_callback_query_handler(send_message_with_link, text="one")
    dp.register_message_handler(get_link, state=menu_1_1.get_back_link)
    dp.register_message_handler(get_new_format, state=menu_1_1.change_format)
    dp.register_callback_query_handler(check_correct_group_format, state=menu_1_1.check_correct_format)
    # Хочет бросить обучение /Сделать возврат
    dp.register_callback_query_handler(send_message_with_link_2, text="two")
    dp.register_message_handler(get_link_2, state=menu_1_1.get_back_link_2)
    dp.register_message_handler(get_cause_return, state=menu_1_1.couse_return)
    dp.register_callback_query_handler(check_correct_return, state=menu_1_1.check_correct_return)
    # Отмена/перенос занятия
    dp.register_callback_query_handler(send_message_with_link_3, text="three", state="*")  # +
    dp.register_message_handler(get_link_3, state=menu_1_1.get_back_link_3)  # +
    dp.register_callback_query_handler(check_twelve_hours, state=menu_1_1.yes_no_3)  # +
    dp.register_message_handler(get_cause_cancellation, state=menu_1_1.concellation)  # +
    dp.register_message_handler(get_old_data, state=menu_1_1.old_data)  # +
    dp.register_message_handler(get_new_data, state=menu_1_1.new_data)  # +
    dp.register_callback_query_handler(check_correct_cancellation, state=menu_1_1.check_correct_cancellation)  # +
    #Оплата ученика
    dp.register_callback_query_handler(send_message_with_link_4, text="four", state="*") #+
    dp.register_message_handler(get_link_4, state=menu_1_1.get_back_link_4)
    dp.register_message_handler(get_question_cash, state=menu_1_1.question_cash)
    dp.register_callback_query_handler(check_correct_question_cash, state=menu_1_1.check_question_cash)
    # dp.register_message_handler(adding_student_by_link,
    #                            CommandStart(deep_link=re.compile(r"^[A-Z]{4,15}$")))

    # # dp.register_message_handler(student_add_name, state=NewUser.state_student_add_name)
    # dp.register_callback_query_handler(teacher_get_email, text="teacher", state=NewUser.state_new_user)
    # dp.register_message_handler(teacher_send_code_to_email, Text(endswith="@kodland.team"),
    #                             state=NewUser.state_teacher_add)
    # dp.register_message_handler(teacher_teacher_get_code, state=NewUser.state_teacher_get_code)
    # dp.register_message_handler(answer_on_bad_mail, state=NewUser.state_teacher_add)
    # dp.register_callback_query_handler(teacher_add_new_group, text="event_add_group_button")  # +
    # dp.register_message_handler(get_group_name, state=NewUser.state_teacher_add_new_group)  # +
    # dp.register_message_handler(get_group_last_lesson, state=NewUser.state_teacher_add_last_lesson)
    # dp.register_message_handler(get_group_weekday, state=NewUser.state_teacher_add_group_day)
    # dp.register_message_handler(get_group_course, state=NewUser.state_teacher_add_group_course)
