from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

"""Клавиатура для не владельца оружия №1"""
text_keyboard = ['Перечень необходимых документов', 'Расписание занятий', 'Дни приема экзамена',
                 'Цена услуги', 'Назад']
kb_not_gun_owner:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_not_gun_owner.add(*[KeyboardButton(i) for i in text_keyboard])