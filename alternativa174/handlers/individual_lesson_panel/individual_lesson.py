from aiogram.types import Message

from config.config import dp
from config.FSM import individual_lesson, start
from work_data.google_sheets.read_data import price_individual_lesson, doc_individual_lesson, \
    schedule_individual_lessons
from alternativa174.keyboards import keyboard_individual_lesson_start, keyboard_yes_not


@dp.message_handler(text=['Записаться на индивидуальное занятие', 'Нет'],
                    state=[start, individual_lesson.exercise])
async def individual_lesson_start(message: Message):
    """
    Стартовая панель индивидуального занятия
    """
    await message.answer('пункт 3. Вы хотите узнать:', reply_markup=keyboard_individual_lesson_start)
    await individual_lesson.exercise.set()


@dp.message_handler(text='Перечень необходимых документов', state=individual_lesson.exercise)
async def required_documents_for_class(message: Message):
    """
    Функция предоставляет пользователю порядок продления и список необходимых документов.
    """
    await message.answer(doc_individual_lesson)


@dp.message_handler(text=['Расписание занятий'], state=individual_lesson.exercise)
async def schedule_lessons(message: Message):
    """
    Функция предоставляет пользователю расписание занятий.
    """
    await message.answer(schedule_individual_lessons)
    await message.answer('Выбрать дату занятия?', reply_markup=keyboard_yes_not)


@dp.message_handler(text='Цена услуги', state=individual_lesson.exercise)
async def price_lesson(message: Message):
    """
    Функция предоставляет пользователю стоимость индивидуального занятия.
    """
    await message.answer(price_individual_lesson, reply_markup=keyboard_individual_lesson_start)
