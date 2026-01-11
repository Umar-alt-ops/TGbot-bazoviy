import asyncio
from aiogram import Bot, Dispatcher

from carbot.start import start_router
from carbot.carprice import menu_router
from carbot.config import token

bot = Bot(token=token)

dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(menu_router)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    
    except KeyboardInterrupt:
        print("Выход")
