import logging 
import asyncio
from aiogram import Bot

from startumhandlers import router, dp
from startumboard import command
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await bot.set_my_commands(command)
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")