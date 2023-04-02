from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

"""Клавиатура для владельца оружия стартовая"""
text_keyboard = ['Продлить разрешение на оружие', 'Повысить навыки владения оружием', 'Назад']
kb_gun_owner_start:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)

kb_gun_owner_start.add(*[KeyboardButton(i) for i in text_keyboard])

"""Клавиатура для продления"""
text_keyboard = ['Порядок продления и необходимые документы', 'Расписание занятий', 'Дни приема экзамена',
                 'Цена услуги', 'Назад']
kb_permit_extension:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_permit_extension.add(*[KeyboardButton(i) for i in text_keyboard])


"""Клавиатура для повышение навыка работы с оружием"""
text_keyboard = ['Программа занятий', 'Перечень необходимых документов', 'Расписание занятий',
                 'Цена услуги', 'Назад']
kb_skill_upgrade:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_skill_upgrade.add(*[KeyboardButton(i) for i in text_keyboard])

"""Клавиатура для выбора оружия"""
text_keyboard = ['Короткоствольное оружие', 'Длинноствольное оружие', 'Отмена']
kb_weapon_selection:ReplyKeyboardMarkup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
kb_weapon_selection.add(*[KeyboardButton(i) for i in text_keyboard])
