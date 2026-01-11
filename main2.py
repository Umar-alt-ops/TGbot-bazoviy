import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.handlers.start import start_router
from app.handlers.menu import menu_router


load_dotenv()

TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(menu_router)

async def main():
    logging.basicConfig(level=logging.INFO)

    await dp.start_polling(bot) 
try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")