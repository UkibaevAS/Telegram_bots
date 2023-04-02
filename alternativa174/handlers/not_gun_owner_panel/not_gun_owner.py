from aiogram import types

from config.config import dp
from config.FSM import not_gun_owner, start
from work_data.google_sheets.read_data import doc_not_gun_owner, price_not_gun_owner, day_and_time_not_gun_owner
from alternativa174.keyboards.not_gun_owners_keyboards import kb_not_gun_owner


@dp.message_handler(text='Первоначальное обучение на право владения оружием', state=start)
async def not_gun_owner_start(message: types.Message):
    """
    Стартовое меню при первичном обучении на право владения оружием
    """
    await message.answer('Вас интересует:', reply_markup=kb_not_gun_owner)
    await not_gun_owner.getting_permission.set()

@dp.message_handler(text='Перечень необходимых документов', state=not_gun_owner.getting_permission)
async def doc_4_lesson(message: types.Message):
    """
    Перечень необходимых документов для первоначального обучения.
    """
    await message.answer(doc_not_gun_owner)


@dp.message_handler(text='Расписание занятий', state=not_gun_owner.getting_permission)
async def schedule_lessons(message: types.Message):
    """
    Функция предоставляет пользователю расписание занятий.
    """
    await message.answer(day_and_time_not_gun_owner)


@dp.message_handler(text='Цена услуги', state=not_gun_owner.getting_permission)
async def price_lesson(message: types.Message):
    """
    Функция предоставляет пользователю стоимость индивидуального занятия.
    """
    await message.answer(price_not_gun_owner)
