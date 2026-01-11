from aiogram import Router, types
from aiogram.filters import Command, CommandStart
from carbot.keyboard import main_keyboard

start_router = Router()

@start_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(
        '''🌟 Добро пожаловать в AutoHub Premium!\n
Нажмите /help чтобы узнать команды бота.'''
        ,
        reply_markup=main_keyboard
    )

@start_router.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("""Чем могу помочь? Нажмите на команды:\n
                        /start\n/len\n/repeat\n/info\n/location\nСлова для ввода:
                        \nфото\nцена ...(введите модель)\n\nгде находится\n\n✨ 🚗 каталог авто
                        \n✨ 📞 контакты\n✨ 🏢 о компании\n\nгде находится\n\nслова приветствия:
                        \n{привет, салам, здарова, ку, hello, hi}\n\nслова для прощания:
                        \n{пока, до встречи, бай, увидимся}\nклиенты:\nали, миша, дастен, алмаз
                        \n(если вы введете имя клиента то бот выведет вам его информацию)""".lstrip())

@start_router.message(Command('info'))
async def info(message: types.Message):
    await message.reply("""Имя:\nУмар\n
Username:\nsomeone\n
ID пользователя:\n20456""")

@start_router.message(Command("len"))
async def length(message: types.Message):
    text = message.text.replace('/len', '').strip()
    if not text:
        await message.reply("Введите текст после команды.")
        return

    await message.reply(f"Длина текста: {len(text)}")

@start_router.message(Command('repeat'))
async def repeat_command(message: types.Message):
    text = message.text.replace("/repeat", "", 1)
    if not text:
        await message.reply("Введите текст после команды.")
        return

    await message.reply(text)

@start_router.message(Command('location'))
async def loc(message: types.Message):
    await message.reply_location(latitude=40.51800714848957, longitude=72.74406373097584)