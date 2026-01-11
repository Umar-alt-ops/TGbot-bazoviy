from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='✨ 🚗 каталог авто'), KeyboardButton(text='✨ 📞 контакты')],
        [KeyboardButton(text='✨ 🏢 о компании')]
    ],
    resize_keyboard=True
)

car_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='👑✨🚘 седаны представительского класса'),
         KeyboardButton(text='💎🌐🚙 премиальные кроссоверы')],
        [KeyboardButton(text='⚡🔋🌱 электромобили'),
         KeyboardButton(text='🏆🔥🏎️ спорткары')]
    ],
    resize_keyboard=True
)
