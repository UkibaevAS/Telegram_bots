from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

""" Клавиатура стартовая"""
text_keyboard = ['Владелец оружия (имею право на его приобретение)', 'Первоначальное обучение на право владения оружием',
                 'Записаться на индивидуальное занятие', 'Перечень необходимых документов',
                 'Теоретические вопросы на экзамен', 'Контактная информация']
start_user_kb: ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
start_user_kb.add(*[KeyboardButton(i) for i in text_keyboard])
