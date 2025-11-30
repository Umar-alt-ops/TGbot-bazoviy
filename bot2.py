import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token

# ReplyKeyboardMarkup - Собирает клавиатуру

bot = Bot(token=token)  # для создания бота, внтури находиться токен
dp = Dispatcher()  # Для того чтобы передать запроc

buttons = [
    [KeyboardButton(text='меню'), KeyboardButton(text='контакты')],
    [KeyboardButton(text='О нас')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку')

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Первое'), KeyboardButton(text='Второе'), KeyboardButton(text='Третье')],
    [KeyboardButton(text='Фастфуд'), KeyboardButton(text='Напитки'), KeyboardButton(text='Салаты')],
], one_time_keyboard=True)

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет!', reply_markup=keyboard)

@dp.message(Command('help'))
async def help(message: types.Message):
    await message.reply('Чем я могу помочь?')

@dp.message(F.text.lower() == 'меню')
async def command_help(message: types.Message):
    await message.reply_photo(photo='https://ru-cafe.ru/content/images/news/menu.jpg', reply_markup=menu_keyboard)

@dp.message(F.text == 'контакты')
async def contacts(message: types.Message):
    await message.reply_contact(phone_number='+996999040587', last_name='Umar', first_name='Muminzhanov')

@dp.message(F.text.in_({'привет', 'првет'}))
async def command_help(message: types.Message):
    await message.reply('Привет')

@dp.message()
async def echo(message: types.Message):
    await message.reply('я вас не понял')

async def main():
    await dp.start_polling(bot) 

try:
    asyncio.run(main())
except KeyboardInterrupt:
    print("выход")