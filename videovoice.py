from aiogram import Bot, Dispatcher, F, types
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
from aiogram.types import FSInputFile
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.environ.get("TOKEN")

video_file = FSInputFile('шаурма.mp4')
voice_file = FSInputFile('voice.ogg')
audio_file = FSInputFile('wedding.mp3')
pdf_file = FSInputFile('google_play.pdf')

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Добро пожаловать!используйте /help чтобы узнать доступные команды.")

@dp.message(Command('my_contact'))
async def contacts(message: Message):
    await message.reply_contact(phone_number='+996555164975', last_name='Muminzhanov', first_name='Umar')


@dp.message(Command('my_location'))
async def loc(message: Message):
    await message.reply("Вот наша локация:")
    await message.reply_location(latitude=40.5287, longitude=72.7938)

@dp.message(Command('photo_car'))
async def cars(message: Message):
    await message.reply_photo(photo='https://i.pinimg.com/736x/fc/01/2e/fc012e328d08d4ac0e7bf0aa628bb795.jpg', 
                              caption="You just want attention")

@dp.message(Command('help'))
async def help_message(message: Message):
    help_text = (
        "Доступные команды:\n"
        "/my_contact - Отправить контактную информацию\n"
        "/my_location - Отправить местоположение\n"
        "/photo_car - Отправить фото машины\n"
        "/voice_only - Отправить голосовое сообщение\n"
        "/audio_only - Отправить аудиофайл с метаданными\n"
        "/document_only - Отправить PDF документ\n"
        "/media_pack - Отправить набор медиафайлов\n"
        "/poll - Отправить опрос\n"
        "/video - Отправить видеофайл\n"
        "/info - Отправить информацию с фото и документом\n"
        "/all - Отправить все типы медиа и опрос"
    )
    await message.answer(help_text)

@dp.message(Command('voice_only'))
async def golos_message(message: Message):
    await message.answer_audio(audio=voice_file)

@dp.message(Command('audio_only'))
async def audio_only(message: Message):
    await message.answer_audio(audio=audio_file,
                               title="Wedding",
                               performer="Unknown Artist",
                               caption="My wedding song")

@dp.message(Command('document_only'))
async def document_only(message: Message):
    await message.answer_document(document=pdf_file)

@dp.message(Command('media_pack'))
async def media_pack(message: Message):
    await message.answer_photo(photo='https://i.pinimg.com/736x/fc/01/2e/fc012e328d08d4ac0e7bf0aa628bb795.jpg')
    await message.answer_video(video=video_file)
    await message.answer_audio(audio=voice_file)
    await message.answer(audio=audio_file,
                         title="Wedding",
                         performer="Unknown Artist",
                         caption="My wedding song")
    
@dp.message(Command('poll'))
async def poll(message: Message):
    await message.answer_poll(
        question="Что вы предпочитаете?",
        options=["Кошки", "Собаки", "Птицы", "Рыбы"],
        is_anonymous=True,
        type="regular"
    )

@dp.message(Command('video'))
async def video(message: Message):
    await message.reply_video(video=video_file)

@dp.message(Command('info'))
async def information(message: Message):
    await message.answer(text='Это фото с машиной:')
    await message.answer_photo(photo='https://i.pinimg.com/736x/fc/01/2e/fc012e328d08d4ac0e7bf0aa628bb795.jpg')
    await message.answer_document(document=pdf_file)

@dp.message(Command('all'))
async def all(message: Message):
    await message.answer(text='Это все чему мы научились:')
    await message.answer_photo(photo='https://i.pinimg.com/736x/fc/01/2e/fc012e328d08d4ac0e7bf0aa628bb795.jpg')
    await message.answer_video(video=video_file)
    await message.answer_audio(audio=voice_file)
    await message.answer_audio(audio=audio_file,
                         title="Wedding",
                         performer="Unknown Artist",
                         caption="My wedding song")
    await message.answer_document(document=pdf_file)
    await message.answer_poll(
        question="Какой язык программирования вам нравится?",
        options=["Python", "JavaScript", "Java", "C++"],
        is_anonymous=True,
        type="regular"
    )


async def main():
    await dp.start_polling(bot)

asyncio.run(main())

'№11'
"Здесь ошибка в том, что переменная и функция названы одинаково - video. Нужно переименовать функцию, например, в send_video."
'№12'
"Потому что функция таким образом перезаписывает файл и он начинает работать некорректно."
'№16'
'''Разница между message.answer() от message.reply() в том что 
message.reply() отвечает на конкретное сообщение пользователя,
в то время как message.answer() просто отправляет сообщение в чат без привязки к конкретному сообщению.'''