from aiogram.types import Message

from config.config import bot, dp, ADMIN_ID
from config.FSM import start, admin, gun_owner, not_gun_owner, individual_lesson
from work_data.google_sheets.read_data import contacts, examination, doc_4_lesson
from keyboards.start_keyboards import start_user_kb
from keyboards.admin_keyboards import kb_admin_start


@dp.message_handler(commands='start', state='*')
async def process_start_help_command(message: Message):
    """
    Стартовое меню
    """
    user_id = str(message.from_user.id)
    if user_id not in ADMIN_ID:
        await message.answer('Привет!\nПопробую Вам помочь.', reply_markup=start_user_kb)
        await message.answer_photo('https://alt174.ru/d/pistolet_roha.jpg')
        await start.start.set()
    else:
        await message.answer('Что делаем?:', reply_markup=kb_admin_start)
        await admin.start.set()


@dp.message_handler(commands='help', state='*')
async def process_start_help_command(message: Message):
    """
    Обработчик команды "/help"
    """
    await message.answer('Все управление ботом осуществляется нажатием на кнопки меню '
                         'расположенные внизу экрана')


@dp.message_handler(commands='contacts', state='*')
async def process_contacts_command(message: Message):
    """
    Обработчик команды "/contacts"
    """
    await message.answer(contacts)


@dp.message_handler(text='Перечень необходимых документов', state=start)
async def required_documents(message: Message):
    """
    Функция предоставляет пользователю общий порядок продления (обучения) и список необходимых документов.
    """
    await message.answer(f'Пройти курс безопасного обращения с оружием могут все граждане РФ,'
                         f' достигшие возраста 21 года.\n{doc_4_lesson}')


@dp.message_handler(text='Теоретические вопросы на экзамен', state=start)
async def send_pdf(message: Message):
    """
    Функция предоставляет перечень теоретических вопросов, выносимых на экзамен.
    """
    await bot.send_document(message.chat.id,
                            document='https://alt174.ru/f/perechen_voprosov_dlya_sajta_po_boso_s_otvetami_15112022g.pdf')


@dp.message_handler(text='Назад',
                    state=[gun_owner.start, not_gun_owner.getting_permission, individual_lesson.exercise])
async def start_menu(message: Message):
    """
    Стартовое меню
    """
    await message.answer('Привет!\nПопробую Вам помочь.', reply_markup=start_user_kb)
    await start.start.set()


@dp.message_handler(text='Дни приема экзамена', state='*')
async def exam_day(message: Message):
    """
    Предоставляет пользователю дни приема экзамена сотрудниками Росгвардии
    """
    await message.answer(examination)


@dp.message_handler(text='Контактная информация', state='*')
async def process_contacts_command(message: Message):
    """
    Предоставляет пользователю контактную информацию ЧОУ ДПО "Альтернатива"
    """
    await message.answer(contacts)


@dp.message_handler(state='*')
async def erroneous_actions(message: Message):
    """
    Обработчик ошибочных нажатий пользователя.
    Перенаправляет на стартовое меню.
    """
    await message.answer('Используйте кнопки меню')
    user_id = str(message.from_user.id)
    if user_id not in ADMIN_ID:
        await message.answer('Привет!\nПопробую Вам помочь.', reply_markup=start_user_kb)
        await message.answer_photo('https://alt174.ru/d/pistolet_roha.jpg')
        await start.start.set()
    else:
        await message.answer('Что делаем?:', reply_markup=kb_admin_start)
        await admin.start.set()
