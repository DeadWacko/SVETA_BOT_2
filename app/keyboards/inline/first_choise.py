from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, inline_keyboard

from app import keyboards

# choice = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(
#             text="Преподаватель",
#             callback_data="teacher"
#         )
#     ],
#     [
#         InlineKeyboardButton(
#             text="ученик",
#             callback_data="student"
#         )
#     ]
# ])
#
# add_group_button = InlineKeyboardButton('Добавить группу ➕', callback_data='event_add_group_button')
# show_stats_button = InlineKeyboardButton('Посмотреть статистику 📄 ', callback_data='event_show_stats_button')
# mailing_button = InlineKeyboardButton('Отправить рассылку 📬 ', callback_data='event_mailing_button')
# jedi_menu_keyboard_markup = InlineKeyboardMarkup().add(add_group_button).add(show_stats_button).add(mailing_button)

# Генерация клавиатуры для выбора команды преподавателя(Предположим их 16)
########################################################################################################################
#Клавиатура выбора команды
team_list = ["Team1", "Team2", "Team3", "Team4", "Team5", "Team6", "Team7", "Team8", "Team9", "Team10", "Team11",
             "Team12", "Team13", "Team14", "Team15","Team16"]
keyboard_list = []
for i in team_list:
    keyboard_list.append(
        [
            InlineKeyboardButton(
                text=f"{i}",
                callback_data=f"{i}"
            )
        ]
        )
team_keyboard = InlineKeyboardMarkup(inline_keyboard=keyboard_list)
########################################################################################################################
#клавиатура ДА/НЕТ
yes = InlineKeyboardButton('Да', callback_data='yes')
no = InlineKeyboardButton('Нет', callback_data='no')
yesno_keyboard_markup = InlineKeyboardMarkup().add(yes).add(no)
########################################################################################################################
#Основная клавиатура меню
questions_about_students = InlineKeyboardButton('Все вопросы, связанные с учениками', callback_data='questions_about_students')
teacher_related_questions= InlineKeyboardButton('Все вопросы,связанные с преподавателями', callback_data='teacher_related_questions')
other_questions= InlineKeyboardButton('Другое, не похожее ни на что', callback_data='other_questions')
menu_1 = InlineKeyboardMarkup().add(questions_about_students).add(teacher_related_questions).add(other_questions)

########################################################################################################################
#ВСЕ ВОПРОСЫ, СВЯЗАННЫЕ С УЧЕНИКАМИ#
one = InlineKeyboardButton('Смена формата обучения', callback_data='one')
two = InlineKeyboardButton('Хочет бросить обучение/сделать возврат', callback_data='two')
three = InlineKeyboardButton('Отмена/перенос', callback_data='three')
four = InlineKeyboardButton('Оплата учеников', callback_data='four')
five = InlineKeyboardButton('Перевод ученика(куда-то)', callback_data='five')
six = InlineKeyboardButton('Прогул занятия', callback_data='six')
seven = InlineKeyboardButton('Изменение данных ученика', callback_data='seven')
eight = InlineKeyboardButton('Ученик не получил сертификат', callback_data='eight')
nine = InlineKeyboardButton('Негатив на преподавателя/кого-то еще', callback_data='nine')
exit = InlineKeyboardButton('EXIT', callback_data='exit')
menu_1_1_keyboard = InlineKeyboardMarkup().add(one).add(two).add(three).add(four).add(five).add(six).add(seven).add(eight).add(nine).add(exit)

