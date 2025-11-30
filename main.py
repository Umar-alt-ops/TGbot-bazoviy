from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio

# Dispatcher - это то бологодоря чему бот отвечает
# CommandStart - нужен для того чтобы давать  старт для нашего бота
# asyncio - нужен для того чтобы твой бот был ассинхронным
# Message - нужет для того чтобы бот принимал текст от юзера

bot = Bot(token='8348943814:AAFaUsVTRBBXAs4ACILQSGEWAAfYxWC69HI') #для создания бота, внтури находиться токен
dp = Dispatcher() #Для того чтобы передать запроc

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Привет!') # А ансвер просто выводит ответ не отвечая нее
    
@dp.message(Command('help'))  
async def help(message:Message):
    await message.reply('Чем я могу помочь?') # Реплай отвечает на сообщение


@dp.message(Command('about'))
async def about(message:Message):
    await message.reply('StartUm - это учебный центр в городе ОШ')

@dp.message(Command('contact'))
async def contact(message:Message):
    await message.reply_contact(phone_number='+996500273979', last_name='Nuraziz', first_name='Makyev')

@dp.message(Command('location'))
async def location(message:Message):
    await message.reply_location(latitude=40.50959574233856, longitude=72.80983119531365 )
   
@dp.message(F.text.lower() == 'абдусамат')
async def abdusamat(message:Message):
    await message.reply('Ученик - 3 месяца')
    
@dp.message(F.text.lower() == 'фото')
async def photo(message:Message):
    await message.reply_photo(photo='https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Bengal_tiger_%28Panthera_tigris_tigris%29_female_3_crop.jpg/960px-Bengal_tiger_%28Panthera_tigris_tigris%29_female_3_crop.jpg')

@dp.message(F.text.lower() == 'стикер')
async def sticker(message: Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAAOFaSgiBxwUFQLwJp6Mcy0JAhV6iIoAAtdKAALnOiFL64QVRPS8nkI2BA')

@dp.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

# async def main():
#     await dp.start_polling(bot)
#                                    # Нужно заполнить вот эти 4 блока
# asyncio.run(main())
