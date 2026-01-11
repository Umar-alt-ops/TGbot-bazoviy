import logging            # подключаем логирование (для вывода информации в консоль)
import asyncio            # модуль для работы с асинхронностью

from aiogram import Bot, Dispatcher, types, F    # импортируем основные классы aiogram
from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart         # фильтр для обработки команды /start
from aiogram import Router                       # Router — система маршрутизации aiogram

router = Router()                                # создаём router — он будет держать обработчики
bot = Bot(token='8339750051:AAH6NbJztij4UnfCSxzgyhLI19tgF-Oju5A')               # создаём объект бота, передаём токен
dp = Dispatcher()  

command = [BotCommand(command="start", description='Начать')]

# --- Обычная клавиатура (ReplyKeyboard) ---
buttons = [                                      # тут создаём список кнопок для обычной клавиатуры
    [KeyboardButton(text="Показать текст")],     # первая кнопка в первом ряду
    [KeyboardButton(text="Очистить экран")],     # вторая кнопка во втором ряду
]
keyboard = ReplyKeyboardMarkup(                  # создаём объект обычной клавиатуры
    keyboard=buttons,                            # передаем кнопки
    resize_keyboard=True                         # клавиатура подстраивается под экран
)

# --- Inline-клавиатура (InlineKeyboard) ---
confirm_buttons = [                              # список inline-кнопок
    [InlineKeyboardButton(text="Да", callback_data="confirm")],   # кнопка "Да" с callback_data
    [InlineKeyboardButton(text="Нет", callback_data="cancel")],   # кнопка "Нет" с callback_data
]

confirm_keyboard = InlineKeyboardMarkup(         # создаём inline-клавиатуру
    inline_keyboard=confirm_buttons              # передаем кнопки
)

# --- Стартовая команда ---
@router.message(CommandStart())                  # обработчик команды /start
async def command_start(message: types.Message): # функция-обработчик
    await message.answer(                        # отправляем сообщение пользователю
        "Привет! 🤖",                            # текст
        reply_markup=keyboard                    # прикрепляем обычную клавиатуру
    )
    
# --- Показ текста ---
@router.message(F.text == "Показать текст")      # обработчик нажатия кнопки "Показать текст"
async def show_text(message: types.Message):     # функция-обработчик
    await message.answer(                        # отправляем сообщение
        "Ты хочешь очистить экран?",             # текст
        reply_markup=confirm_keyboard            # ПРИКРЕПЛЯЕМ INLINE-КНОПКИ!
    )
    
# --- Кнопка "Очистить экран" ---
@router.message(F.text == "Очистить экран")      # обработчик нажатия кнопки "Очистить экран"
async def ask_clear(message: types.Message):     # функция-обработчик
    await message.answer(                        # отправляем сообщение
        "Ты уверен?",                            # текст
        reply_markup=confirm_keyboard            # показываем inline-кнопки
    )
    
# --- Inline callback: подтверждение ---
@router.callback_query(F.data == "confirm")      # обработчик inline-события, если callback_data == "confirm"
async def callback_confirm(callback: types.CallbackQuery):   # callbackQuery содержит инфу о нажатии
    await callback.message.edit_text(            # изменяем текст старого сообщения
        "Экран очищен! 🧹"                       # новый текст
    )
    await callback.answer()                      # закрываем кружочек "thinking..."


# --- Inline callback: отмена ---
@router.callback_query(F.data == "cancel")       # обработчик inline-события, если callback_data == "cancel"
async def callback_cancel(callback: types.CallbackQuery):   # callbackQuery обработчик
    await callback.message.edit_text(            # изменяем текст старого сообщения
        "Действие отменено ❌"                   # новый текст
    )
    await callback.answer()                      # закрываем кружочек "thinking..."

# --- Запуск ---
async def main():                                # главная асинхронная функция
    logging.basicConfig(level=logging.INFO)      # включаем логирование
    dp.include_router(router)                    # регистрируем Router в диспетчере
    await bot.set_my_commands(command)           # устанавливаем команду /start
    await dp.start_polling(bot)                  # запускаем бота для приёма обновлений

# запуск асинхронного приложения
try:
    asyncio.run(main())                          # запускаем main
except KeyboardInterrupt:                        # если нажали Ctrl+C
    print("Выход")