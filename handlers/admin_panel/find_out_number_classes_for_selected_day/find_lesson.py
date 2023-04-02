from aiogram_calendar import simple_cal_callback, SimpleCalendar
from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from config.config import dp
from config.FSM import admin
from working_with_calendar.selected_data import check_number_classes


@dp.callback_query_handler(simple_cal_callback.filter(), state=admin.view)
async def view_selected_date(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Функция, просмотра занятий на выбранную пользователем дату
    """
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        result = await check_number_classes(date, state)
        if result:
            for i_rec in result:
                await callback_query.message.answer(f'\nДата занятия: {i_rec.get("Дата занятия")}'
                                                    f'\nВремя занятия: {i_rec.get("Время занятия")}'
                                                    f'\nТелефон: {"+" + i_rec.get("Телефон")}'
                                                    f'\nИмя: {i_rec.get("Имя")}'
                                                    f'\nФамилия: {i_rec.get("Фамилия")}')
        else:
            await callback_query.message.answer('Занятий на этот день нет.\nВыберите другую дату',
                                                reply_markup=await SimpleCalendar().start_calendar())
