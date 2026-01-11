import logging
import asyncio
from aiogram import Bot, Dispatcher, types, F
import os 
from dotenv import load_dotenv
from inlinehandlers import router
from replyinline import command

load_dotenv()

TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)

dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(router)
    await bot.set_my_commands(command)
    await dp.start_polling(bot)

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("Выход")