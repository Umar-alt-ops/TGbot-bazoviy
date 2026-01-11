from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu_router = Router()

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='первое'), KeyboardButton(text='второе'), KeyboardButton(text='третье')],
    [KeyboardButton(text='фастфуд'), KeyboardButton(text='напитки'), KeyboardButton(text='салаты')]
], one_time_keyboard=True, resize_keyboard=True, input_field_placeholder='Выберите опцию')

@menu_router.message(F.text == 'меню')
async def command_help(message: types.Message):
    await message.answer_photo(photo='https://ru-cafe.ru/content/images/news/menu.jpg')

@menu_router.message(F.text == 'меню')
async def contacts(message: types.Message):
    await message.answer('Наши контакты: +996 627 198 034')

@menu_router.message(F.text.lower() == 'о нас')
async def about(message: types.Message):
    await message.answer('Мы молодая компания, которая делает крутые проекты!')

@menu_router(F.text.in_({'привет', 'првет'}))
async def command_help(message: types.Message):
    await message.reply('Привет')

@menu_router.message()
async def echo(message: types.Message):
    await message.answer('Я вас не понял')

