import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types

from aiogram.filters import CommandStart
from dotenv import load_dotenv

#Загружаем переменные окружения из .env файла
load_dotenv()

#Берем токен из окружения
TOKEN = os.environ.get("token")

bot = Bot(token=TOKEN)
dp = Dispatcher()

#хендлер /start без роутеров
@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Бот запущен и готов к работе!')

async def main():
    # Настройка логгера
    logging.basicConfig(level=logging.INFO)

    #Запуск бота

    await dp.start_polling(bot)
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")

'''
* 'DEBUG' - подробная откладка
* 'INFO' - обычная информация(старт бота, действя)
* 'WARNING' - предупреждения
* 'ERROR' - ошибки
* 'CRITICAL' - критические ошибки
'''
