from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


"""Клавиатура для индивидуального занятия №1"""
text_keyboard = ['Перечень необходимых документов', 'Расписание занятий', 'Цена услуги', 'Назад']
keyboard_individual_lesson_start:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
keyboard_individual_lesson_start.add(*[KeyboardButton(i) for i in text_keyboard])


"""Клавиатура для индивидуального занятия №1_2"""
text_keyboard = ['Да', 'Нет']
keyboard_yes_not:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
keyboard_yes_not.add(*[KeyboardButton(i) for i in text_keyboard])



"""Клавиатура для получения номера телефона """
keyboard_get_contact:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
button_1: KeyboardButton = KeyboardButton('Отправить номер', request_contact=True)
button_2: KeyboardButton = KeyboardButton('Отмена')
keyboard_get_contact.add(button_1, button_2)

"""Клавиатура для подтверждения данных"""
text_keyboard = ['Записаться на занятие', 'Назад']
keyboard_data_confirmation:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_data_confirmation.add(*[KeyboardButton(i) for i in text_keyboard])

"""Клавиатура для оплаты"""
keyboard_payment:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_payment.add('500 руб')
keyboard_payment.add('Назад')

"""Клавиатура выбора времени занятия"""
text_keyboard = ['9.30', '11.00', '12.30', 'Отмена']
keyboard_choice_time:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
keyboard_choice_time.add(*[KeyboardButton(i) for i in text_keyboard])





