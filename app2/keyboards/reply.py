from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

buttons = [
    [KeyboardButton(text='📚 Возможности бота'), KeyboardButton(text='🧠 Информация')],
    [KeyboardButton(text='⚙️ Настройки'), KeyboardButton(text='❌ Закрыть меню')]
]   
reply_keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите одну из кнопок')
