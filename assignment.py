from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import token
import asyncio
bot = Bot(token=token)  # для создания бота, внтури находиться токен
dp = Dispatcher()

buttons = [
    [KeyboardButton(text='О нас'), KeyboardButton(text='Направления')],
    [KeyboardButton(text='Контакты')]
]
keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True, one_time_keyboard=True, input_field_placeholder='Выберите одну из кнопок')

directions = """Выбирайте направление, которое вам по душе:
— Backend  
— Frontend
- математика(на англ.языке)
— Ментальная арифметика  
— Русский язык"""

directions_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Backend'), KeyboardButton(text='Frontend')],
    [KeyboardButton(text='Математика (на англ. языке)'), KeyboardButton(text='Ментальная арифметика')],
    [KeyboardButton(text='Русский язык')]
], one_time_keyboard=True)

backend_keyboard = '''Backend — это внутренняя часть сайта, серверная логика и базы данных.  
Стоимость: 4500 сом в месяц.  
Обучение: 7 месяцев.'''

frontend_keyboard = '''В направлении frontend вы научитесь работать с веб сайтами, страницами и много чего др.
- Стоимость курса: 4000 сщм в месяц
- Срок обучения: 6 месяцев'''

math_keyboard = '''Математика на английском языке — это курс, который помогает детям изучать школьную математику и одновременно улучшать английский язык.  
Стоимость: 3500 сом в месяц.  
Обучение: 5 месяцев.'''

mental = '''Ментальная арифметика — это развитие быстрого счёта, логики, внимания и памяти через специальные техники устного счёта.  
Стоимость: 4000 сом в месяц.  
Обучение: 6 месяцев.'''

russian = '''Курс русского языка направлен на развитие грамотности, улучшение письма, чтения и разговорных навыков.  
Стоимость: 3000 сом в месяц.  
Обучение: 4 месяца.'''
courses = {
    'backend': backend_keyboard,
    'frontend': frontend_keyboard,
    'математика (на англ. языке)': math_keyboard,
    'ментальная арифметика': mental,
    'русский язык': russian
}
    

@dp.message(CommandStart())
async def start(message: types.Message):
    await message.answer('Привет!', reply_markup=keyboard)

@dp.message(F.text.lower() == 'о нас')
async def us(message: types.Message):
    await message.reply("""StartUm - это учебный центр в городе ОШ
У нас есть много направлений: Если хотите их посмотреть, нажмите на кнопку "Направления".""")

@dp.message(F.text.lower() == 'направления')
async def direct(message: types.Message):
    await message.reply(directions, reply_markup=directions_keyboard)

@dp.message(F.text.lower() == 'контакты')
async def contacts(message: types.Message):
    await message.reply_contact(phone_number='+996999040587', last_name='Umar', first_name='Muminzhanov')

@dp.message()
async def course_info(message: types.Message):
    text = message.text.lower()
    if text in courses:
        await message.reply(courses[text])

async def main():
    await dp.start_polling(bot)

asyncio.run(main())