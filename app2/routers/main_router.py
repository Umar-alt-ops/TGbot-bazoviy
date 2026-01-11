import logging
import asyncio
import os
from aiogram import Bot, Dispatcher, types
from app2.handlers.start import starting_router
from app2.handlers.menu import men_router
from aiogram.filters import CommandStart
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot)
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")