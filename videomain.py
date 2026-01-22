from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
import asyncio
from aiogram.types import FSInputFile
from dotenv import load_dotenv
import os
load_dotenv()

TOKEN = os.environ.get("TOKEN")

video_file = FSInputFile('video.mp4')
voice_file = FSInputFile('voice.ogg')
audio_file = FSInputFile('music.mp3')
pdf_file = FSInputFile('file.pdf')

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("""Привет!\n
Я учебный бот.\n
Напиши /menu чтобы увидеть команды""")

@dp.message(Command('menu'))
async def menu(message: Message):
    menu_text = (
        "Доступные команды:\n"
        "/contact – контакт\n"
        "/location – локация\n"
        "/photo – фото\n"
        "/media – видео, аудио и документ\n"
        "/poll – опрос\n"
    )
    await message.answer(menu_text)

@dp.message(Command('contact'))
async def send_contact(message: Message):
    await message.reply_contact(phone_number='+1234567890', last_name='Doe', first_name='John')
    await message.answer("Это мой контакт!")

@dp.message(Command('photo'))
async def send_photo(message: Message):
    await message.reply_photo(photo='https://i.pinimg.com/736x/7f/dc/a0/7fdca0a0ce3ca4c308b9ce7fd02b5bea.jpg',
                              caption='Пример фото')
    
@dp.message(Command('media'))
async def send_media(message: Message):
    await message.answer_video(video=video_file)
    await message.answer_voice(voice=voice_file)
    await message.answer_audio(audio=audio_file,
                               title="Funk no batidao",
                               performer="MC Fioti")
    await message.answer_document(document=pdf_file)

@dp.message(Command('poll'))
async def send_poll(message: Message):
    await message.answer_poll(
        question="Ты понял прошлый урок?",
        options=["Да","Частично", "Нет"],
        is_anonymous=False,
        type="regular"
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())