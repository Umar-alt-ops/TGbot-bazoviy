import asyncio
from aiogram import Bot, Dispatcher


from example.menu import menu_router
from example.start import start_router

bot = Bot(token='8339750051:AAH6NbJztij4UnfCSxzgyhLI19tgF-Oju5A')

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

