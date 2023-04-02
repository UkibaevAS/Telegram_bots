from aiogram_calendar import simple_cal_callback, SimpleCalendar
from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery, ContentType
from aiogram.dispatcher import FSMContext

from config.config import dp
from config.FSM import individual_lesson, start
from working_with_calendar.selected_data import check_number_classes, check_lesson_time
from work_data.mongodb.write_data.write_data import write_data
from keyboards.individual_lesson_keyboards import keyboard_choice_time, keyboard_get_contact, keyboard_yes_not
from keyboards.start_keyboards import start_user_kb


@dp.message_handler(text=['Да', 'Отмена'], state=[individual_lesson.exercise, individual_lesson.choice_time])
async def choice_day(message: Message):
    """
    Календарь для выбора даты занятия.
    """
    await message.answer('Дни занятий: Среда', reply_markup=ReplyKeyboardRemove())
    await message.answer('Пятница и Суббота', reply_markup=await SimpleCalendar().start_calendar())
    await individual_lesson.exercise.set()


@dp.callback_query_handler(simple_cal_callback.filter(), state=individual_lesson.exercise)
async def choice_data(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    """
    Функция выбора даты занятия. Исходя из возможности записи (результат функции check_number_classes)
    определяет дальнейший вариант событий для пользователя
    """
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        if await check_number_classes(date, state) == True:
            await individual_lesson.choice_time.set()
            await callback_query.message.answer('Выберите время занятия', reply_markup=keyboard_choice_time)
        elif await check_number_classes(date, state) == 'Ошибка ввода':
            await callback_query.message.answer('Дни занятий: Среда\nПятница и Суббота',
                                                reply_markup=await SimpleCalendar().start_calendar())
        else:
            await callback_query.message.answer(f'На {date.strftime("%d/%m/%Y")} все занятия уже заняты',
                                                reply_markup=await SimpleCalendar().start_calendar())



@dp.message_handler(text=['Назад', 'Отмена'], state=[individual_lesson.choice_time, individual_lesson.pay])
async def choice_time(message: Message):
    """
    Функция выбора времени занятия. Исходя из возможности записи (результат функции check_lesson_time)
    определяет дальнейший вариант событий для пользователя

    """
    await message.answer('Выберите время занятия', reply_markup=keyboard_choice_time)
    await individual_lesson.choice_time.set()


@dp.message_handler(text=['9.30', '11.00', '12.30'], state=individual_lesson.choice_time)
async def lesson_time(message: Message, state=FSMContext):
    """
    Функция выбора времени занятия. Исходя из возможности записи (результат функции check_lesson_time)
    определяет дальнейший вариант событий для пользователя.

    """
    if await check_lesson_time(message.text, state):
        async with state.proxy() as info:
            info['Время занятия'] = message.text
            await message.answer(f'{info["Дата занятия"]} в {info["Время занятия"]}\nРазрешите телеграм получить '
                                 f'Ваш номер телефона для регистрации Вас на занятие',
                                 reply_markup=keyboard_get_contact)
            await individual_lesson.pay.set()
    else:
        await message.answer('Это время уже занято. Выбрать другое время занятия?',
                             reply_markup=keyboard_choice_time)


@dp.message_handler(content_types=ContentType.CONTACT, state=individual_lesson.pay)
async def process_get_phone(message: Message, state: FSMContext):
    """
    Функция получения номера телефона пользователя.

    """
    await write_data(message, state)
    await message.answer('Успешно. Ждем Вас на занятие.', reply_markup=start_user_kb)
    await start.start.set()
    # await message.answer('В целях исключения ложных регистраций требуется внести предоплату в размере 500 рублей.'
    #                      '\nЭта сумма будет учтена при оплате занятия.'
    #                      '\nВНИМАНИЕ! В случае неявки на занятие внесенная предоплата возврату не подлежит!'
    #                      '\nЮ Касса    Оплачиваем?', reply_markup=keyboard_yes_not)


@dp.message_handler(text='Да', state=individual_lesson.pay)
async def payment(message: Message):
    """
    Функция оплаты занятия
    """
    await message.answer('Успешная оплата. Тут пока заглушка')
    await message.answer('Привет!\nПопробую Вам помочь.', reply_markup=start_user_kb)
    await start.start.set()


@dp.message_handler(text='Нет', state=individual_lesson.pay)
async def not_payment(message: Message):
    """
    Отказ от оплаты, возврат на стартовое меню
    """

    await message.answer('Отказ от оплаты')
    await message.answer('Привет!\nПопробую Вам помочь.', reply_markup=start_user_kb)
    await start.start.set()
