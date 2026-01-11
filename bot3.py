import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='Меню'), KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]
]

keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите кнопку')

menu_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Первое'), KeyboardButton(text='Второе')],
    [KeyboardButton(text='Напитки'), KeyboardButton(text='Фастфуд')]
])
photos = [
    'https://sushikoto.ru/wp-content/uploads/2019/04/2-m.jpg',
    'https://api.chaihona1.ru/files/entity/menu_items/100000003/1700000052/med_418724.jpg',
    'https://notivory.com/upload/medialibrary/305/30589066aefb75192d98a394b8ee2d22.jpg',
    'https://m.dom-eda.com/uploads/images/catalog/item/53275a4f46/c4f7252f9e_1000.jpg'
]
students = {'абдусамат': 'ученик 5 месяца',
            'умар': 'ученик 6 месяца', 
             'абдуллох': 'Ученик в 7 классе 13 лет'}

foods = {'первое': 'https://www.remenu.ru/menuboard/ico-menuboard-tablet175.jpg',
         'второе': 'https://cf2.ppt-online.org/files2/slide/l/L9PKxT7XqiGcQrp5BmJ0fCtewsoHDFzl4Vvn1U/slide-1.jpg',
         'напитки': 'https://cf2.ppt-online.org/files2/slide/l/L9PKxT7XqiGcQrp5BmJ0fCtewsoHDFzl4Vvn1U/slide-6.jpg',
         'фастфуд': 'https://i.pinimg.com/736x/6a/62/62/6a626230a8fc828849cd4bb4dfc0da9b.jpg'}

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Приветсвую в нашем телеграм боте!', reply_markup=keyboard)
40.50964468493593, 72.80989556973532
@dp.message(Command('location'))
async def loc(message: types.Message):
    await message.reply_location(latitude=40.514, longitude=72.816)
    
@dp.message(Command('help'))
async def how(message: types.Message):
    await message.reply('Чем могу помочь?', reply_markup=keyboard)

@dp.message(F.text.lower() == 'меню')
async def menu(message: types.Message):
    await message.reply_photo(photo='https://gcdn.tomesto.ru/img/place/000/026/318/kafe-vstrecha-na-kirova_c2dc1_full-320520.jpg', reply_markup=menu_keyboard)

@dp.message(F.text.lower() == 'о нас')
async def Startum(message: types.Message):
    await message.reply("StartUm - это учебный центр в городе Ош. В этом центре есть много разных направлений")

@dp.message(F.text.in_({"привет", "салам", "ку", "здарова"}))
async def say_hello(message: types.Message):
    await message.reply("И тебе привет 🤝")

@dp.message(F.text.in_({"пока", "бай", "до встречи"}))
async def bye(message: types.Message):
    await message.reply('До связи!')


@dp.message(F.text.lower() == 'фото')
async def photo(message: types.Message):
    await message.reply_photo(random.choice(photos))

@dp.message(Command("repeat"))
async def repeat_command(message: types.Message):
    text = message.text.replace("/repeat", "", 1)

    if not text:
        await message.reply("Введите текст после команды.")
        return

    await message.reply(text)

@dp.message(F.text.lower() == 'стих')
async def stix(message: types.Message):
    await message.reply("""Я помню чудное мгновенье:
Передо мной явилась ты,
Как мимолетное виденье,
Как гений чистой красоты.

В томленьях грусти безнадежной,
В тревогах шумной суеты,
Звучал мне долго голос нежный
И снились милые черты.

Шли годы. Бурь порыв мятежный
Рассеял прежние мечты,
И я забыл твой голос нежный,
Твои небесные черты.""")

@dp.message(F.sticker)
async def get_stick_id(message: types.Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

@dp.message(Command('info'))
async def info(message: types.Message):
    await message.reply('Имя: Умар\nUsername:Umash117\nID:201008')


@dp.message(Command("len"))
async def length(message: types.Message):
    text = message.text.replace('/len', '').strip()

    if not text:
        await message.reply("Введите текст после команды.\nПример: /len Привет")
        return

    await message.reply(f"Длина текста: {len(text)}")

@dp.message(F.text.lower() == 'контакты')
async def contact(message: types.Message):
    await message.reply_contact(phone_number='+996999040587', last_name='Umar', first_name='Muminzhanov')

@dp.message()
async def universal_handler(message: types.Message):
    text = message.text.lower()

    if text in foods:
        await message.reply_photo(foods[text])
        return

    if text in students:
        await message.reply(students[text])
        return

    await message.reply("Не нашёл такую команду 🙂")


async def main():
    await dp.start_polling(bot)
    
asyncio.run(main())