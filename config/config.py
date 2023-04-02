import os
import dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.redis import RedisStorage2

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')

# Создаем хранилище
storage: RedisStorage2 = RedisStorage2()

# Создаем объекты бота и диспетчера

bot: Bot = Bot(token=BOT_TOKEN, parse_mode='HTML')
dp: Dispatcher = Dispatcher(bot, storage=storage)


async def set_main_menu(dp: Dispatcher):
    # Создаем список с командами для кнопки menu
    main_menu_commands = [
        types.BotCommand(command='/start', description='Рестарт бота'),
        types.BotCommand(command='/help', description='Справка по работе бота'),
        types.BotCommand(command='/contacts', description='Контактная информация')
    ]
    await dp.bot.set_my_commands(main_menu_commands)
