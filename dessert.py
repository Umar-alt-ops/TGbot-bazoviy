import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from dotenv import load_dotenv
import os
import logging
import random

dessert_keyboard = [
    [KeyboardButton(text='🍰 Каталог'), KeyboardButton(text='💰 Цены'),
     KeyboardButton(text='🛒 Оформить заказ')],
    [KeyboardButton(text='📞 Контакты'), KeyboardButton(text='📍 Адрес'),
     KeyboardButton(text='ℹ️ О студии')]
]

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cakes_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='🎂 Торты'),
            KeyboardButton(text='🍬 Макаруны'),
            KeyboardButton(text='🍮 Пирожные')
        ],
        [
            KeyboardButton(text='🥗 Без сахара'),
            KeyboardButton(text='⭐ Хиты продаж'),
            KeyboardButton(text='⬅️ Главное меню')
        ]
    ],
    resize_keyboard=True
)


cakes = {'🎂 Торты': 'https://i.pinimg.com/1200x/96/60/20/9660205776983a49e9b5d275be53a5ce.jpg',
         '🍬 Макаруны': 'https://i.pinimg.com/736x/dc/12/cd/dc12cd38442bd7f6c8b4493403295ada.jpg',
         '🍮 Пирожные': 'https://i.pinimg.com/736x/2a/bc/2c/2abc2c7b57387ce4fd11907d81ed5601.jpg',
         '🥗 Без сахара': 'https://i.pinimg.com/736x/4d/10/02/4d100289c0833ea8142623137768c166.jpg',
         '⭐ Хиты продаж': 'https://i.pinimg.com/736x/1d/6c/9b/1d6c9b030af9fc895d07b9710d66401c.jpg'}

prices = {
    "velvet": 4800,
    "pistachio": 5200,
    "эклер": 320,
    "macaron": 180,
    "truffle": 400
}

cakes2 = {
    '🎂 Торты': (
        "🎂 Торты:\n"
        "1. Velvet Cake - 4800₽\n"
        "2. Pistachio Cake - 5200₽\n"
        "3. Truffle Cake - 400₽\n"
    ),
    '🍬 Макаруны': (
        "🍬 Макаруны:\n"
        "1. Macaron - 180₽\n"
    ),
    '🍮 Пирожные': (
        "🍮 Пирожные:\n"
        "1. Éclair - 320₽\n"
    ),
    '🥗 Без сахара': (
        "🥗 Без сахара:\n"
        "1. Без сахара торт - 4800₽\n"
    ),
    '⭐ Хиты продаж': (
        "⭐ Хиты продаж:\n"
        "1. Velvet Cake - 4800₽\n"
        "2. Macaron - 180₽\n"
    )
}

number_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='📲 Отправить номер', request_contact=True),
            KeyboardButton(text='⬅️ Главное меню')]
    ],
    resize_keyboard=True
)


price_keyboard = [
    [KeyboardButton(text='💰 Узнать цену'), KeyboardButton(text='📸 Показать фото')],
    [KeyboardButton(text='🛒 Заказать'), KeyboardButton(text='⬅️ Назад')]
]

keyboard = ReplyKeyboardMarkup(
    keyboard=dessert_keyboard,
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder="Выберите пункт меню"
)

load_dotenv()
logging.basicConfig(level=logging.INFO)
TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    logging.info(f"Пользователь {user_id} запустил бота")
    await message.reply("""> Добро пожаловать в SweetLab Boutique 🍰
> Я могу отвечать **только на вопросы, связанные с нашей кондитерской.
> Выберите действие с помощью кнопок ниже.""", reply_markup=keyboard)

@dp.message(F.text.casefold() == "🍰 каталог")
async def catalog_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил каталог")

    await message.reply("""> Выберите категорию десертов:\n
* 🎂 Торты
* 🍬 Макаруны
* 🍮 Пирожные
* 🥗 Без сахара
* ⭐ Хиты продаж
""", reply_markup=cakes_keyboard)
    
@dp.message(F.text.in_(cakes.keys()))
async def cake_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} выбрал категорию: {message.text}")
    await message.reply_photo(photo=cakes[message.text],
                        caption=cakes2[message.text],
                        reply_markup=price_keyboard)

@dp.message(F.text.casefold() == "💰 цены")
async def prices_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил цены")
    await message.reply("> Чтобы узнать цену, напишите:\n> `цена <название десерта>")

@dp.message(F.text.lower().startswith("цена"))
async def price_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил цену")
    text = message.text.lower().replace("цена ", "")
    if not text.startswith("цена"):
        return
    parts = text.split(maxsplit=1)

    if len(parts) != 2:
        await message.reply(
            "Используйте формат: цена <название>"
        )
        return

    dessert = parts[1]

    if dessert not in prices:
        await message.reply(
            "Такого десерта нет в нашем каталоге 🍰"
        )
        return

    price = prices[dessert]
    await message.reply(
        f"Цена «{dessert.capitalize()}»: {price} сом"
    )


@dp.message(F.text.casefold() == "⬅️ главное меню")
async def main_menu_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} вернулся в главное меню")
    await message.reply("> Вы вернулись в главное меню.", reply_markup=keyboard)

@dp.message(F.text.casefold() == "📸 Показать фото")
async def show_photo_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил фото десертов")
    await message.reply_photo(random.choice(cakes.values()))

@dp.message(F.text.casefold() == "🛒 оформить заказ")
async def order_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} оформляет заказ")
    await message.reply("> Напишите название десерта, который хотите заказать.")
    des_text = message.text.lower()
    if des_text in cakes:
        await message.reply("Заказ принят! Наш менеджер скоро свяжется с вами.")
    else:   
        await message.reply("> Мы принимаем заказы только на десерты из каталога 🍰")

@dp.message(F.text.casefold() == "📞 контакты")
async def contacts_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил контакты")
    await message.reply("> Вы можете оставить номер телефона для связи:", reply_markup=number_keyboard)

@dp.message(F.text.casefold() == "📍 адрес")
async def address_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил адрес")
    await message.reply_location(latitude=40.528055, longitude=72.794286)

@dp.message(F.text.casefold() == "ℹ️ о студии")
async def about_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} запросил информацию о студии")
    await message.reply("""> SweetLab Boutique — кондитерская студия премиум-класса.
> Работаем с 2018 года.""")

@dp.message(F.text.in_({'привет', 'салам', 'hello', 'hi'}))
async def say_hi(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} поздоровался")
    await message('> Здравствуйте! Чем могу помочь?')

@dp.message(Command("info"))
async def information(message: types.Message):
    await message.reply("""Имя создателя:\nУмар\n
Username:\nUmar2010\nID:Umw3465""")
    
@dp.message(Command("len"))
async def length(message: types.Message):
    text = message.text.replace('/len', '').strip()
    if not text:
        await message.reply("Введите текст после команды.")
        return

    await message.reply(f"Длина текста: {len(text)}")

@dp.message(F.sticker)
async def stick(message: types.Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

@dp.message()
async def unknown_handler(message: types.Message):
    logging.info(f"Пользователь {message.from_user.id} ввел неизвестную команду: {message.text}")
    await message.reply("""> Я могу отвечать только на вопросы, связанные с нашей кондитерской 🍰
> Пожалуйста, используйте кнопки меню.""")
    

async def main():
    await dp.start_polling(bot)

asyncio.run(main())
