from aiogram.types import Message

from keyboards.gun_owner_keyboards import kb_gun_owner_start
from config.config import dp
from config.FSM import gun_owner, start


@dp.message_handler(text=['Владелец оружия (имею право на его приобретение)', 'Назад'],
                    state=[start.start, gun_owner.prolongation, gun_owner.skill_upgrade])
async def gun_owner_start(message: Message):
    """
    Стартовая панель владельца оружием
    """
    await message.answer('Как владелец оружия Вы хотите:', reply_markup=kb_gun_owner_start)
    await gun_owner.start.set()
