from aiogram.types import Message

from config.config import dp
from config.FSM import gun_owner
from work_data.google_sheets.read_data import price_prolongation, doc_4_lesson, day_and_time_4prolongation
from alternativa174.keyboards.gun_owner_keyboards import kb_permit_extension


@dp.message_handler(text='Продлить разрешение на оружие', state=gun_owner.start)
async def procedure_renewal_permit(message: Message):
    """
    Стартовая панель владельца оружия при продлении разрешения.
    """
    await message.answer('Вы хотите узнать:', reply_markup=kb_permit_extension)
    await gun_owner.prolongation.set()


@dp.message_handler(text='Порядок продления и необходимые документы', state=gun_owner.prolongation)
async def required_documents_for_renewal(message: Message):
    """
    Функция предоставляет пользователю порядок продления и список необходимых документов.
    """
    await message.answer(doc_4_lesson)


@dp.message_handler(text='Расписание занятий', state=gun_owner.prolongation)
async def timetable(message: Message):
    """
    Функция предоставляет пользователю расписание занятий.
    """
    await message.answer(day_and_time_4prolongation)


@dp.message_handler(text='Цена услуги', state=gun_owner.prolongation)
async def renewal_price(message: Message):
    """
    Функция предоставляет пользователю стоимость услуги по продлению разрешения.
    """
    await message.answer(price_prolongation)
