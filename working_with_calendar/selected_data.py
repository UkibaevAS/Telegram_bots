import datetime
from aiogram.dispatcher import FSMContext

from work_data.google_sheets.read_data import day_training
from work_data.mongodb.read_data.read_data import check_len, read_data


async def check_number_classes(date: datetime, state: FSMContext):
    """
    Функция для проверки выбранной даты занятия.
    1. для администратора:
        1.1 в режиме "удаления записи":
        - выбранная дата м.б. >= текущему времени
        1.2 в режиме "просмотра записей":
        - выбранная дата не зависит на текущего времени (для возможности просмотра архива)
    2. для пользователя:
        - запись в выбранную дату возможна не менее чем за 12 часов до начала занятия

    :param date: Выбранная пользователем дата
    :rtype: class datetime.datetime
    :param state: Конечный автомат (для записи выбранной даты)
    :rtype: class FSMContext
    :return: строка, булевое значение или объект Курсор (полученный из БД MongoDB)

    """
    if await state.get_state() in 'admin:delete':
        query = {'Дата занятия': date.strftime("%d/%m/%Y")}
        rec_lesson = await read_data(query)
        cursor = rec_lesson.clone()
        if len(list(cursor)) == 0:
            return True
        else:
            async with state.proxy() as info:
                info['Дата занятия'] = date.strftime("%d/%m/%Y")
            return rec_lesson

    elif await state.get_state() in 'admin:view':
        query = {'Дата занятия': date.strftime("%d/%m/%Y")}
        rec_lesson = await read_data(query)
        cursor = rec_lesson.clone()
        if len(list(cursor)) != 0:
            return rec_lesson
        else:
            return False

    else:
        if date <= datetime.datetime.now() + datetime.timedelta(hours=12):
            return 'Ошибка ввода'
        if date.strftime("%a") not in day_training:
            return 'Ошибка ввода'
        query = {'Дата занятия': date.strftime("%d/%m/%Y")}
        if await check_len(query) >= 3:
            return False
        async with state.proxy() as info:
            info['Дата занятия'] = date.strftime("%d/%m/%Y")
            return True


async def check_lesson_time(time: str, state: FSMContext) -> bool:
    """
    Функция для проверки возможности записи на выбранное пользователем время занятия.

    :param time: Выбранное пользователем время
    :rtype: str
    :param state: Конечный автомат (для записи выбранного времени)
    :rtype: class FSMContext
    :return: булевый тип
    :rtype: bool
    """
    async with state.proxy() as info:
        query = {'Дата занятия': info.get('Дата занятия')}
        rec_lesson = await read_data(query)
        flag = True
        for i_rec in rec_lesson:
            if time in i_rec.values():
                flag = False
                break
        if flag:
            info['Время занятия'] = time
        return flag
