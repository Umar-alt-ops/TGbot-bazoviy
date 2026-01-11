import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='✨ 🚗 каталог авто'), KeyboardButton(text='✨ 📞 контакты')], 
    [KeyboardButton(text='✨ 🏢 о компании')]
]

car = [
    [KeyboardButton(text='👑✨🚘 седаны представительского класса'), KeyboardButton(text='💎🌐🚙 премиальные кроссоверы')],
    [KeyboardButton(text='⚡🔋🌱 электромобили'), KeyboardButton(text='🏆🔥🏎️ спорткары')]
]

sportcars = {'👑✨🚘 седаны представительского класса': 'https://i.pinimg.com/736x/4d/2f/63/4d2f6316268ad9b858329e6d0605a2a3.jpg',
             '💎🌐🚙 премиальные кроссоверы': 'https://i.pinimg.com/1200x/08/e8/77/08e877db466f6ebf11af506aab5268d8.jpg',
             '⚡🔋🌱 электромобили': 'https://i.pinimg.com/736x/d9/51/5b/d9515b1b13482a6ca8fd0e179c05a5bb.jpg',
             '🏆🔥🏎️ спорткары': 'https://i.pinimg.com/736x/b7/d7/69/b7d769fef11008c04fc7108b88da0fc5.jpg'}

car_texts = {
    '👑✨🚘 седаны представительского класса': (
        "👑 Седаны представительского класса:\n"
        "• Mercedes-Benz S-Class — 125 000 $ 💰\n"
        "• BMW 7 Series — 118 000 $ 💵\n"
        "• Audi A8 — 110 000 $ 💸"
    ),
    '💎🌐🚙 премиальные кроссоверы': (
        "💎 Премиальные кроссоверы:\n"
        "• BMW X7 — 102 000 $ 💸\n"
        "• Mercedes GLS — 105 000 $ 💵\n"
        "• Range Rover Vogue — 135 000 $ 💰💰"
    ),
    '⚡🔋🌱 электромобили': (
        "⚡ Электромобили:\n"
        "• Tesla Model X — 98 000 $ 💸\n"
        "• Mercedes EQS — 110 000 $ 💰💵\n"
        "• Porsche Taycan — 130 000 $ 💰💰"
    ),
    '🏆🔥🏎️ спорткары': (
        "🏆 Спорткары:\n"
        "• Porsche 911 Turbo S — 205 000 $ 💰💰\n"
        "• Nissan GT-R — 125 000 $ 💵\n"
        "• BMW M4 Competition — 92 000 $ 💸"
    )
}

lamba = [
    'https://i.pinimg.com/736x/ef/eb/73/efeb736d52befd3da4edb4a03bc428f5.jpg',
    'https://i.pinimg.com/736x/c0/7b/19/c07b1929b0d2a15a7b08e1916370173b.jpg',
    'https://i.pinimg.com/736x/c8/c9/65/c8c9657498ac80b96a4d5df6b937c7f3.jpg',
    'https://i.pinimg.com/736x/78/7a/2b/787a2beb4bd4ec5de686045f8783c018.jpg',
    'https://i.pinimg.com/736x/45/02/45/450245a731656ab6fe33d43756dc2b96.jpg'
]

prices = {
    "g-class": 165000,
    "urus": 260000,
    "taycan": 130000,
    "m8": 145000,
    "s-class": 125000,
}

clients = {
    "али": "Покупка: BMW X7 — 2 месяца назад",
    "миша": "Покупка: Mercedes S-Class — 1 месяц назад",
    "дастен": "Покупка: Porsche Taycan — 3 месяца назад",
    "алмаз": "Покупка: Audi A8 — 5 месяцев назад"
}

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку')


@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('🌟 Добро пожаловать в премиальный автосалон AutoHub Premium!\n📌 Выберите интересующий раздел ниже.', reply_markup=keyboard)

@dp.message(Command('help'))
async def helping(message: types.Message):
    await message.answer('🤝 Чем могу помочь? Выберите действие: /start\n/')

@dp.message(F.text.lower() == '✨ 🚗 каталог авто')
async def cars(message: types.Message):
    await message.reply_photo(photo='https://i.pinimg.com/736x/4d/2f/63/4d2f6316268ad9b858329e6d0605a2a3.jpg', reply_markup=ReplyKeyboardMarkup(
        keyboard=car,
        resize_keyboard=True
    )
)

@dp.message(F.text.in_({'✨ 🏢 о компании'}))
async def comp(message: types.Message):
    await message.reply('''👑 AutoHub Premium
Салон люксовых автомобилей с 2010 года
🔹 Мы специализируемся на новых премиальных авто
🔹 Предлагаем эксклюзивные поставки под заказ
🔹 Реализуем индивидуальную комплектацию автомобиля под клиента
🚘✨ Премиум. Исключительность. Стиль.''')
    
@dp.message(F.text.casefold() == '✨ 📞 контакты')
async def cont(message: types.Message):
    await message.reply_contact(phone_number='+996 500 123 456', last_name='Фасад', first_name='Ismailov')

@dp.message(F.text.lower() == 'где находится')
async def place(message: types.Message):
    await message.reply('''📍г. Бишкек, пр. Чуй 228
🕒 Работаем: 09:00–21:00 ежедневно''')

@dp.message(F.text.in_({"привет", "салам", "здарова", "ку", "hello", "hi"}))
async def say_hello(message: types.Message):
    await message.reply('''👋 Здравствуйте! Добро пожаловать в AutoHub Premium
✨ Мир люксовых автомобилей начинается здесь.''')

@dp.message(F.text.in_({"пока", "до встречи", "бай", "увидимся"}))
async def bye(message: types.Message):
    await message.reply('> До скорой встречи! 🚗💨')

@dp.message(F.text.lower() == 'фото')
async def photo(message: types.Message):
    await message.reply_photo(random.choice(lamba))

@dp.message(F.text.lower().startswith("цена"))
async def qwerty(message: types.Message):
    text2 = message.text.lower().replace("цена ", "")

    if text2 in prices:
        await message.reply(f"Цена {text2.upper()} — {prices[text2]} $")
    else:
        await message.reply("Модель не найдена в базе!")

@dp.message(F.sticker)
async def stick(message: types.Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

@dp.message(Command('info'))
async def info(message: types.Message):
    await message.reply("""Имя:\nУмар\n
                        Username:\nsomeone\n
                        ID пользователя:\n20456""")

@dp.message(Command("len"))
async def length(message: types.Message):
    text = message.text.replace('/len', '').strip()
    if not text:
        await message.reply("Введите текст после команды.")
        return

    await message.reply(f"Длина текста: {len(text)}")

@dp.message(Command('repeat'))
async def repeat_command(message: types.Message):
    text = message.text.replace("/repeat", "", 1)
    if not text:
        await message.reply("Введите текст после команды.")
        return

    await message.reply(text)

@dp.message(Command('location'))
async def loc(message: types.Message):
    await message.reply_location(latitude=40.51800714848957, longitude=72.74406373097584)

@dp.message()
async def universal(message: types.Message):
    text = message.text.lower()

    for key in sportcars:
        if text == key.lower():
            await message.reply_photo(
                photo=sportcars[key],
                caption=car_texts[key]
            )
            return
        
    if text in clients:
        await message.reply(clients[text])
        return
    
    await message.reply('Клиента нет в базе!')

async def main():
    await dp.start_polling(bot)

asyncio.run(main())