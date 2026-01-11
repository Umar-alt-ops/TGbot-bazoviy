import asyncio
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token
from example.keyboard import keyboard

start_router = Router()

@start_router.message(CommandStart())
async def command_start(message: types.Message):
    await message.answer('Привет', reply_markup=keyboard)


@start_router.message(Command('help'))
async def command_help(message: types.Message):
    await message.reply("Чем могу помочь?")

