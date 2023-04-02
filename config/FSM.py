from aiogram.dispatcher.filters.state import State, StatesGroup


class start(StatesGroup):
    start = State()               # Начальное состояние общее


class admin(StatesGroup):
    start = State()               # Начальное состояние администратора
    view = State()                # Состояние просмотра записей
    record = State()              # Состояние внесения записи
    delete = State()              # Состояние удаления записи


class gun_owner(StatesGroup):
    start = State()               # Начальное состояние владельца оружия
    prolongation = State()        # Состояние продления разрешения на оружие
    skill_upgrade = State()       # Состояние повышения навыков
    type_weapon = State()         # Состояние выбора оружия


class not_gun_owner(StatesGroup):
    getting_permission = State()  # Состояние получения разрешения на оружие


class individual_lesson(StatesGroup):
    exercise = State()            # Состояние записи на занятия
    choice_time = State()         # Состояние выбора времени занятия
    pay = State()                 # Состояние оплаты
