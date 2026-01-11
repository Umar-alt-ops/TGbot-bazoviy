import logging
from aiogram import Router, F, types
from app2.keyboards.reply import reply_keyboard

info_router = Router()
@info_router.message(F.text == "🧠 Информация")
async def info_command(message: types.Message):
    try:
        logging.info(f"Пользователь {message.from_user.id} использовал /info")

        await message.reply(
            """Этот бот создан для логирования действий пользователей и демонстрации возможностей Aiogram.\n
Имя разработчика: Муминжанов Умар\n
Версия бота: 1.0.0""",
            reply_markup=reply_keyboard
        )

    except Exception:
        logging.exception("Ошибка в info_command")
        await message.reply("⚠️ Ошибка при показе информации.")