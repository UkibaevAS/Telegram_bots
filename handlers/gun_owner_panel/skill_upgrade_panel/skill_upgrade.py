from aiogram.types import Message

from config.config import dp
from config.FSM import gun_owner
from work_data.google_sheets.read_data import schedule_individual_lessons, doc_4skill_upgrade, \
    price_4skill_upgrade, handgun_program, long_gun_program

from keyboards.gun_owner_keyboards import kb_skill_upgrade, kb_weapon_selection
from keyboards.individual_lesson_keyboards import keyboard_individual_lesson_start


@dp.message_handler(text=['Повысить навыки владения оружием', 'Отмена', 'Нет'],
                    state=[gun_owner.start, gun_owner.skill_upgrade, gun_owner.type_weapon])
async def gun_owner_skill_upgrade(message: Message):
    """
    Стартовая панель владельца оружия при повышении навыка владения оружием.
    """
    await message.answer('Вы хотите хотите узнать:', reply_markup=kb_skill_upgrade)
    await gun_owner.skill_upgrade.set()


@dp.message_handler(text='Программа занятий', state=gun_owner.skill_upgrade)
async def weapon_selection(message: Message):
    """
    Функция предоставляет пользователю выбор вида оружия.
    """
    await message.answer('Какой вид оружия интересует?', reply_markup=kb_weapon_selection)
    await gun_owner.type_weapon.set()


@dp.message_handler(text='Короткоствольное оружие', state=gun_owner.type_weapon)
async def handgun(message: Message):
    """
    Функция предоставляет пользователю программу подготовки с короткоствольным оружием.
    """
    await message.answer(handgun_program, reply_markup=kb_weapon_selection)


@dp.message_handler(text='Длинноствольное оружие', state=gun_owner.type_weapon)
async def long_gun(message: Message):
    """
    Функция предоставляет пользователю программу подготовки с длинноствольным оружием.
    """
    await message.answer(long_gun_program, reply_markup=kb_weapon_selection)


@dp.message_handler(text='Перечень необходимых документов', state=gun_owner.skill_upgrade)
async def required_documents_improve_skills(message: Message):
    """
    Функция предоставляет пользователю порядок продления и список необходимых документов.
    """
    await message.answer(doc_4skill_upgrade)


@dp.message_handler(text='Цена услуги', state=gun_owner.skill_upgrade)
async def skill_upgrade_price(message: Message):
    """
    Функция предоставляет пользователю стоимость услуг при повышении навыка владения оружием.
    """
    await message.answer(price_4skill_upgrade)


@dp.message_handler(text='Расписание занятий', state=gun_owner.skill_upgrade)
async def get_timetable_classes(message: Message):
    """
    Функция предоставляет пользователю расписание занятий.
    """
    await message.answer(schedule_individual_lessons, reply_markup=keyboard_individual_lesson_start)
