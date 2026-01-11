from aiogram import Router, types, F
from carbot.keyboard import car_keyboard
import random

menu_router = Router()

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


@menu_router.message(F.text.casefold() == '✨ 🚗 каталог авто')
async def catalog(message: types.Message):
    await message.answer_photo(
        photo='https://i.pinimg.com/736x/4d/2f/63/4d2f6316268ad9b858329e6d0605a2a3.jpg',
        reply_markup=car_keyboard
    )


@menu_router.message(F.text.casefold() == '✨ 📞 контакты')
async def contacts(message: types.Message):
    await message.answer_contact(
        phone_number='+996 500 123 456',
        first_name='Ismailov',
        last_name='Фасад'
    )

@menu_router.message(F.text.casefold() == '✨ 🏢 о компании')
async def comp(message: types.Message):
    await message.reply('''👑 AutoHub Premium
Салон люксовых автомобилей с 2010 года
🔹 Мы специализируемся на новых премиальных авто
🔹 Предлагаем эксклюзивные поставки под заказ
🔹 Реализуем индивидуальную комплектацию автомобиля под клиента
🚘✨ Премиум. Исключительность. Стиль.''')
    
@menu_router.message(F.text.lower() == 'где находится')
async def place(message: types.Message):
    await message.reply('''📍г. Бишкек, пр. Чуй 228
🕒 Работаем: 09:00–21:00 ежедневно''')

@menu_router.message(F.text.in_({"привет", "салам", "здарова", "ку", "hello", "hi"}))
async def say_hello(message: types.Message):
    await message.reply('''👋 Здравствуйте! Добро пожаловать в AutoHub Premium
✨ Мир люксовых автомобилей начинается здесь.''')

@menu_router.message(F.text.in_({"пока", "до встречи", "бай", "увидимся"}))
async def bye(message: types.Message):
    await message.reply('> До скорой встречи! 🚗💨')

@menu_router.message(F.text.lower() == 'фото')
async def photo(message: types.Message):
    await message.reply_photo(random.choice(lamba))

@menu_router.message(F.text.lower().startswith("цена"))
async def qwerty(message: types.Message):
    text2 = message.text.lower().replace("цена ", "")

    if text2 in prices:
        await message.reply(f"Цена {text2.upper()} — {prices[text2]} $")
    else:
        await message.reply("Модель не найдена в базе!")

@menu_router.message(F.sticker)
async def stick(message: types.Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')


@menu_router.message()
async def universal(message: types.Message):
    text = message.text.casefold()

    for key in sportcars:
        if text == key.casefold():
            await message.reply_photo(
                photo=sportcars[key],
                caption=car_texts[key]
            )
            return
        
    if text in clients:
        await message.reply(clients[text])
        return

    await message.reply('Клиента нет в базе!')