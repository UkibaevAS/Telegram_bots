from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from work_data.mongodb.database_access import col


async def write_data(message: Message, state: FSMContext) -> None:
    if await state.get_state() in 'individual_lesson:pay':
        async with state.proxy() as info:
            info['Телефон'] = message.contact.phone_number
            info['Имя'] = message.contact.first_name
            info['Фамилия'] = message.contact.last_name
            info['username'] = message.chat.username
            info['user_id'] = message.contact.user_id
            info['Дата внесения записи'] = message.date.strftime('%d-%m-%Y %H:%M')

    elif await state.get_state() in 'admin:record':
        user_data = message.text.split()
        async with state.proxy() as info:
            info['Телефон'] = await format_phone(user_data[0])
            info['Имя'] = user_data[1].capitalize()
            if len(user_data) == 3:
                info['Фамилия'] = user_data[2].capitalize()
            info['Дата внесения записи'] = message.date.strftime('%d-%m-%Y %H:%M')
            info['username'] = None
            info['user_id'] = None

    col.insert_one(await state.get_data())


async def format_phone(data: str) -> str:
    """
    Функция для форматирования номера телефона. Приводит номер к виду: +79001112233
    :param data: номер телефона
    :rtype: str
    :return: номер телефона
    :rtype: str
    """
    return data if data[0] == '7' else '7' + data[1:]
