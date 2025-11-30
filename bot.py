from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio

bot = Bot(token='8339750051:AAH6NbJztij4UnfCSxzgyhLI19tgF-Oju5A') #для создания бота, внтури находиться токен
dp = Dispatcher() #Для того чтобы передать запроc

@dp.message(CommandStart())
async def start(message:Message):
    await message.answer('Привет!') 

@dp.message(Command('name'))
async def name(message:Message):
    await message.reply('Меня зовут Умар!')

@dp.message(F.text.lower() == 'привет')
async def howareyou(message:Message):
    await message.reply('Привет, как дела?')

@dp.message(F.text.lower() == 'пока')
async def bye(message:Message):
    await message.reply('До встречи!')

@dp.message(Command('contact'))
async def contact(message:Message):
    await message.reply_contact(phone_number='+996999040587', last_name='Umar', first_name='Muminzhanov')

@dp.message(F.text.lower() == 'фото')
async def photo(message:Message):
    await message.reply_photo(photo='https://avangardplastik.ru/upload/iblock/fad/iob4k2l256pppb85t1emr9t53jbpp0g0.jpg')
@dp.message(Command('mylocation'))
async def mylocation(message:Message):
    await message.reply_location(latitude=40.528343, longitude=72.794465 )

@dp.message(F.text.lower() == 'кот')
async def cat(message:Message):
    await message.reply_photo(photo='https://icatcare.org/app/uploads/2018/07/Thinking-of-getting-a-cat.png')

@dp.message(F.text.lower() == 'стик')
async def stick(message: Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAANWaSgxP18vD3aAFmEF7Z9lq1twdWoAAk9RAAL8allLUb62eAJxRwM2BA')

@dp.message(F.text.lower() == 'стикер')
async def sticker(message: Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAANfaSgyUR3Xrc3_AgOibdddTq2sJkcAAg9SAAIP-lBLtOCtoWIXyDM2BA')

@dp.message(F.sticker)
async def get_sticker_id(message: Message):
    await message.answer(f"file_id:\n<code>{message.sticker.file_id}</code>", parse_mode='HTML')

@dp.message(F.text.lower() == 'как дела?')
async def WhatsApp(message:Message):
    await message.reply('У меня все отлично! А у тебя?')

@dp.message(Command('StartUm'))
async def startum(message:Message):
    await message.reply('StartUm - это учебный центр в городе ОШ')
    await message.reply_photo(photo='https://scontent-waw2-2.cdninstagram.com/v/t51.2885-19/471846532_1975158456328308_4654827683022820017_n.jpg?stp=dst-jpg_s320x320_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=scontent-waw2-2.cdninstagram.com&_nc_cat=100&_nc_oc=Q6cZ2QHnSenu_vhgZLkGGlW5Do7zGNxg2CWRoFzY9les_5dYRklnkh-Siihxn4hCgIEum_g&_nc_ohc=YtHfqSPCJuwQ7kNvwFjL3Hp&_nc_gid=i7396MBIu41qsMz3CxB-ug&edm=AOQ1c0wBAAAA&ccb=7-5&oh=00_AfiVjXnM4XK7x5bi0YeYzlMRCu9iegwhp56fFJZdSZJnsw&oe=692FB2C3&_nc_sid=8b3546')
    await message.reply_location(latitude=40.50947616097112, longitude=72.80986639562305)

@dp.message(Command('info'))
async def info(message:Message):
    await message.reply('Имя: Умар\nВозраст: 15 лет\nГород: Ош')

@dp.message(Command('Profile'))
async def profile(message:Message):
    await message.reply_contact(phone_number='+996999040587', last_name='Muminzhanov', first_name='Umar')
    await message.reply_photo(photo='https://avangardplastik.ru/upload/iblock/fad/iob4k2l256pppb85t1emr9t53jbpp0g0.jpg')
    await message.reply_location(latitude=40.50947616097112, longitude=72.80986639562305 )
    await message.reply_sticker(sticker='CAACAgIAAxkBAANfaSgyUR3Xrc3_AgOibdddTq2sJkcAAg9SAAIP-lBLtOCtoWIXyDM2BA')

@dp.message(F.text.lower() == 'меню')
async def menu(message:Message):
    await message.reply('1 - Фото\n2 - Локация\n3 - контакт\n4 - Стикер')

@dp.message(F.text.in_({'1', '2', '3', '4'}))
async def menu_options(message:Message):
    if message.text == '1':
        await message.reply_photo(photo='https://avangardplastik.ru/upload/iblock/fad/iob4k2l256pppb85t1emr9t53jbpp0g0.jpg')
    elif message.text == '2':
        await message.reply_location(latitude=40.528343, longitude=72.794465 )
    elif message.text == '3':
        await message.reply_contact(phone_number='+996999040587', last_name='Umar', first_name='Muminzhanov')
    elif message.text == '4':
        await message.reply_sticker(sticker='CAACAgIAAxkBAANfaSgyUR3Xrc3_AgOibdddTq2sJkcAAg9SAAIP-lBLtOCtoWIXyDM2BA')

@dp.message(F.text.lower() == 'погода')
async def weather(message:Message):
    await message.reply_sticker(sticker='CAACAgIAAxkBAAOBaSnPvdyNCohaqMjsfRVGI2GK2qgAAj0BAAIw1J0REPfKB3GSj-42BA')

@dp.message()
async def message(message:Message):
    await message.reply('Я не понимаю, напиши /help чтобы узнать команды.')

async def main():
    await dp.start_polling(bot)
                                   # Нужно заполнить вот эти 4 блока
asyncio.run(main())