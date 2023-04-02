from aiogram_calendar import simple_cal_callback, SimpleCalendar
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher import FSMContext

from config.config import dp
from config.FSM import admin
from working_with_calendar.selected_data import check_number_classes, check_lesson_time
from work_data.mongodb.write_data.write_data import write_data
from alternativa174.keyboards import kb_admin_start
from alternativa174.keyboards import keyboard_choice_time


@dp.callback_query_handler(simple_cal_callback.filter(), state=admin.record)
async def selected_date(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Функция выбора даты занятия. Исходя из возможности записи (результат функции check_number_classes)
    определяет дальнейший вариант событий для пользователя
    """
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        if await check_number_classes(date, state) == True:
            await callback_query.message.answer('Выберите время занятия', reply_markup=keyboard_choice_time)
        elif await check_number_classes(date, state) == 'Ошибка ввода':
            await callback_query.message.answer('Дни занятий: Среда\nПятница и Суббота',
                                                reply_markup=await SimpleCalendar().start_calendar())
        else:
            await callback_query.message.answer(f'На {date.strftime("%d/%m/%Y")} все занятия уже заняты',
                                                reply_markup=await SimpleCalendar().start_calendar())


@dp.message_handler(text=['9.30', '11.00', '12.30'], state=admin.record)
async def lesson_time(message: Message, state: FSMContext):
    """
    Функция выбора времени занятия. Исходя из возможности записи (результат функции check_lesson_time)
    определяет дальнейший вариант событий для пользователя

    """
    if await check_lesson_time(message.text, state) == True:
        async with state.proxy() as info:
            await message.answer(
                f'{info.get("Дата занятия")} в {message.text}\nВведите номер телефона (пример: 89021112233),'
                f' имя и фамилию (через пробел) для внесения записи', reply_markup=ReplyKeyboardRemove())

    else:
        await message.answer('Это время уже занято. Выбрать другое время занятия?',
                             reply_markup=keyboard_choice_time)


@dp.message_handler(state=admin.record)
async def add_rec_lesson(message: Message, state: FSMContext):
    """
    Фукнкция, оповещающая пользователя об (не)успешной записи в БД.
    """
    if len(message.text.split()) > 1:
        await write_data(message, state)
        await message.answer('Запись успешно добавлена.', reply_markup=kb_admin_start)
    else:
        await message.answer('Проверьте корректность введенных данных\nЧто делаем?:', reply_markup=kb_admin_start)

    await admin.start.set()
