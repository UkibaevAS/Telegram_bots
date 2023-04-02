from aiogram_calendar import SimpleCalendar
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from config.config import dp
from config.FSM import admin
from keyboards.admin_keyboards import kb_admin_start


@dp.message_handler(text=['Узнать количество занятий', 'Внести запись о занятии',
                          'Удалить запись о занятии'],
                    state=[admin.start, admin.view, admin.record, admin.delete])
async def admin_state_action(message: Message, state: FSMContext):
    """
    Присвоение статуса администратора, в зависимости от его выбора (просмотр, внесение или удаление записи)
    """
    async with state.proxy() as info:
        info.clear()
    if message.text == 'Внести запись о занятии':
        await admin.record.set()
    elif message.text == 'Узнать количество занятий':
        await admin.view.set()
    elif message.text == 'Удалить запись о занятии':
        await admin.delete.set()

    await message.answer('Выберите интересующую дату', reply_markup=await SimpleCalendar().start_calendar())


@dp.message_handler(text=['Отмена'], state=[admin.start, admin.view, admin.record, admin.delete])
async def admin_start(message: Message):
    """
    Стартовое меню панели администратора
    """
    await message.answer('Что делаем?:', reply_markup=kb_admin_start)
    await admin.start.set()
