import logging
from aiogram import Router
from aiogram.types import Message

menu_router = Router()


@menu_router.message(lambda message: message.text == "Каталог")
async def catalog_handler(message: Message):
    logging.info(f"Пользователь {message.from_user.id} нажал кнопку Каталог")
    await message.answer("📦 Здесь будет каталог")


@menu_router.message(lambda message: message.text == "Профиль")
async def profile_handler(message: Message):
    logging.info(f"Пользователь {message.from_user.id} нажал кнопку Профиль")
    await message.answer("👤 Это ваш профиль")


@menu_router.message(lambda message: message.text == "Помощь")
async def help_handler(message: Message):
    logging.info(f"Пользователь {message.from_user.id} нажал кнопку Помощь")
    await message.answer("❓ Чем могу помочь?")
