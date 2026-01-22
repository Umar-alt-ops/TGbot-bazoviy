import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from aiogram import Router
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()

command = [BotCommand(command="start", description='Начать')]

user_tasks = {}
waiting_for_task = set()


reply_board = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Добавить задачу")],
        [KeyboardButton(text="Показать задачи")],
        [KeyboardButton(text="Очистить список")]
    ],
    resize_keyboard=True
)


inline_board = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Подтвердить", callback_data="confirm"),
            InlineKeyboardButton(text="Отменить", callback_data="cancel")
        ]
    ]
)


@router.message(CommandStart())
async def start(message: types.Message):
    await message.answer("Привет! Выбери действие:", reply_markup=reply_board)


@router.message(lambda m: m.text == "Добавить задачу")
async def add_task(message: types.Message):
    user_id = message.from_user.id
    waiting_for_task.add(user_id)
    await message.answer("Введите текст задачи:")


@router.message(lambda m: m.from_user.id in waiting_for_task)
async def save_task(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_tasks:
        user_tasks[user_id] = []
    user_tasks[user_id].append(message.text)
    waiting_for_task.remove(user_id)
    await message.answer("Задача добавлена ", reply_markup=reply_board)


@router.message(lambda m: m.text == "Показать задачи")
async def show_tasks(message: types.Message):
    tasks = user_tasks.get(message.from_user.id, [])

    if not tasks:
        await message.answer("Список задач пуст")
        return

    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                text=" ".join(task.split()[:2]),
                callback_data=f"task_{i}"
            )]
            for i, task in enumerate(tasks)
        ]
    )

    await message.answer("Выберите задачу:", reply_markup=kb)

@router.callback_query(lambda c: c.data.startswith("task_"))
async def task_detail(callback: types.CallbackQuery):
    index = int(callback.data.split("_")[1])
    task = user_tasks[callback.from_user.id][index]
    await callback.message.answer(task)
    await callback.answer()

@router.message(lambda m: m.text == "Очистить список")
async def clean(message: types.Message):
    await message.answer("Вы уверены, что хотите очистить список задач?", reply_markup=inline_board)

@router.callback_query(lambda c: c.data == "confirm")
async def callback_confirm(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    user_tasks[user_id] = []
    await callback.message.edit_text("Список задач очищен ")
    await callback.answer()

@router.callback_query(lambda c: c.data == "cancel")
async def callback_cancel(callback: types.CallbackQuery):
    await callback.message.edit_text("Очистка отменена ")
    await callback.answer()


async def main():                               
    logging.basicConfig(level=logging.INFO)     
    dp.include_router(router)                   
    await bot.set_my_commands(command)          
    await dp.start_polling(bot)                

try:
    asyncio.run(main())                         
except KeyboardInterrupt:                       
    print("Выход")