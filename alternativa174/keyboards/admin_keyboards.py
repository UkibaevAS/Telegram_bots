from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


"""Клавиатура для админа"""
text_keyboard = ['Узнать количество занятий', 'Внести запись о занятии', 'Удалить запись о занятии']
kb_admin_start:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_admin_start.add(*[KeyboardButton(i) for i in text_keyboard])



"""Клавиатура выбора действий"""
text_keyboard = ['Узнать количество занятий', 'Внести запись о занятии', 'Удалить запись о занятии']
kb_admin_choise:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_admin_choise.add(*[KeyboardButton(i) for i in text_keyboard])
