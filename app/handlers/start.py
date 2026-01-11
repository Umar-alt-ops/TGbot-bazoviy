import logging
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.keyboards.main import main_keyboard

start_router = Router()


@start_router.message(CommandStart())
async def start_handler(message: Message):
    user_id = message.from_user.id

    logging.info(f"Пользователь {user_id} запустил бота")

    await message.answer(
        text="Привет! Выбери пункт меню 👇",
        reply_markup=main_keyboard
    )
