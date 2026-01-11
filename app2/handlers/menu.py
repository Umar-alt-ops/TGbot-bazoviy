import logging
from aiogram import Router, F, types
from aiogram.filters import Command

from app2.keyboards.reply import reply_keyboard

men_router = Router()


@men_router.message(Command("help"))
async def help_command(message: types.Message):
    try:
        logging.info(f"Пользователь {message.from_user.id} использовал /help")

        await message.reply(
            "📌 Список доступных команд:\n\n"
            "/start — запуск бота\n"
            "/help — список команд\n"
            "/menu — главное меню",
            reply_markup=reply_keyboard
        )

    except Exception:
        logging.error("Ошибка в help_command")
        await message.reply("⚠️ Ошибка при показе помощи.")


@men_router.message(Command("menu"))
async def show_menu(message: types.Message):
    try:
        logging.info(f"Пользователь {message.from_user.id} открыл меню")

        await message.reply(
            "📂 Главное меню:",
            reply_markup=reply_keyboard
        )

    except Exception:
        logging.error("Ошибка в show_menu")
        await message.reply("⚠️ Ошибка при открытии меню.")


@men_router.message(F.text == "📚 Возможности бота")
async def features(message: types.Message):
    try:
        logging.info(f"Пользователь {message.from_user.id} открыл раздел возможностей")

        await message.reply(
            "🤖 Возможности бота:\n\n"
            "• Обработка команд\n"
            "• Кнопочное меню\n"
            "• Логирование\n"
            "• Обработка ошибок",
            reply_markup=reply_keyboard
        )

    except Exception:
        logging.error("Ошибка в features handler")
        await message.answer("⚠️ Не удалось показать возможности.")


@men_router.message(F.text == "⚙️ Настройки")
async def settings(message: types.Message):
    try:
        logging.info(f"Пользователь {message.from_user.id} открыл раздел настроек")
        

        await message.reply(
            "⚙️ Раздел настроек в разработке.",
            reply_markup=reply_keyboard
        )

    except Exception:
        logging.error("Ошибка в settings handler")
        await message.answer("⚠️ Ошибка при открытии настроек.")


@men_router.message(F.text == "❌ Закрыть меню")
async def close_menu(message: types.Message):
    try:
        logging.info(f"Пользователь {message.from_user.id} закрыл меню")
        
        await message.reply("❌ Меню закрыто.")
    except Exception:
        logging.error("Ошибка в close_menu handler")
        await message.reply("⚠️ Ошибка при закрытии меню.")

