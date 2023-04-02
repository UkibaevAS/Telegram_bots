from aiogram import executor
from config.config import set_main_menu
from handlers import *





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)
