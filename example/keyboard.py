from aiogram import Router, types, F
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text='меню'), KeyboardButton(text='контакты')],
    [KeyboardButton(text='о нас')]
]

keyboard = ReplyKeyboardMarkup(
    keyboard=buttons,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Выберите кнопку'
)
