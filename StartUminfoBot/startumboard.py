from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

command = [BotCommand(command="start", description='Начать')]

classic_buttons = [
    [KeyboardButton(text="Арифметика"), KeyboardButton(text="Русский язык"), KeyboardButton(text="Продлёнка"), KeyboardButton(text="Программирование")],
    [KeyboardButton(text="Английский язык"), KeyboardButton(text="Контакты"), KeyboardButton(text="Адрес")],
]

classic_board = ReplyKeyboardMarkup(
    keyboard=classic_buttons,
    resize_keyboard=True
)

inline = [
    [InlineKeyboardButton(text="Записаться", callback_data="confirm")],
    [InlineKeyboardButton(text="Назад", callback_data="cancel")],
]

inl_board = InlineKeyboardMarkup(
    inline_keyboard=inline
)
