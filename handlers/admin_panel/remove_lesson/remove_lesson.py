from aiogram_calendar import simple_cal_callback, SimpleCalendar
from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext

from config.config import dp
from config.FSM import admin
from work_data.mongodb.read_data.read_data import read_data
from work_data.mongodb.delete_data.delete_data import delete_data
from working_with_calendar.selected_data import check_number_classes
from keyboards.individual_lesson_keyboards import keyboard_choice_time


@dp.callback_query_handler(simple_cal_callback.filter(), state=admin.delete)
async def chose_date(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Функция для просмотра занятий на выбранную пользователем дату
    """
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        result = await check_number_classes(date, state)
        if result == True:
            await callback_query.message.answer('Занятий на этот день нет\nВыберите интересующую дату',
                                                reply_markup=await SimpleCalendar().start_calendar())
        else:
            for i_rec in result:
                await callback_query.message.answer(f'\nДата занятия: {i_rec.get("Дата занятия")}'
                                                    f'\nВремя занятия: {i_rec.get("Время занятия")}'
                                                    f'\nТелефон: {i_rec.get("Телефон")}'
                                                    f'\nИмя: {i_rec.get("Имя")}'
                                                    f'\nФамилия: {i_rec.get("Фамилия")}')
            await callback_query.message.answer('Запись о занятии на какое время требуется удалить?',
                                                reply_markup=keyboard_choice_time)


@dp.message_handler(text=['9.30', '11.00', '12.30'], state=admin.delete)
async def del_lesson_time(message: Message, state=FSMContext):
    """
    Функция для удаления занятия на выбранное пользователем время
    """
    async with state.proxy() as info:
        query = {'Дата занятия': info['Дата занятия']}
        if await delete_data(message.text, await read_data(query)):
            await message.answer('Запись удалена', reply_markup=keyboard_choice_time)
        else:
            await message.answer(f'{info["Дата занятия"]} в {message.text}\nТакого занятия нет в записях',
                                 reply_markup=keyboard_choice_time)
