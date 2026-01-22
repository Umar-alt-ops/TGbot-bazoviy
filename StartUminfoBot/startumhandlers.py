from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart
from aiogram import Router
from startumboard import inl_board, classic_board

dp = Dispatcher()
router = Router()

@router.message(CommandStart())
async def startum_start(message: types.Message):
    await message.answer_photo(photo='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTAnznuSBrrKlBQcEUu5RQsjpe1Jfnoe7Nxyg&s', caption="""Привет! Это бот учебного центра StartUm 📚
Выбери направление, и я расскажу подробнее!""", reply_markup=classic_board)

@router.message(F.text.lower() == "программирование")
async def program(message: types.Message):
    await message.reply("""> 💻 Программирование\n
> Возраст: 12+\n
> Длительность: 7 месяц\n
> Изучаем Python, структуры данных, проекты.\n
""", reply_markup=inl_board)

@router.message(F.text.lower() == "арифметика")
async def arif(message: types.Message):
    await message.reply("""Арифметика\n
Возраст: 6–10 лет\n
Длительность: 6 месяцев\n
Счёт, логика, задачи, основы математики для уверенного обучения в школе.""", reply_markup=inl_board)
    
@router.message(F.text.lower() == "русский язык")
async def rus(message: types.Message):
    await message.reply("""Русский язык\n
Возраст: 6–12 лет\n
Длительность: 7 месяцев\n
Грамматика, орфография, чтение, развитие речи и письмо без ошибок.""", reply_markup=inl_board)
    
@router.message(F.text.lower() == "продлёнка")
async def prod(message: types.Message):
    await message.reply("""🕒 Продлёнка\n
Возраст: 6–10 лет\n
Длительность: учебный год\n
Помощь с домашними заданиями, игры, отдых и развитие в безопасной обстановке.""", reply_markup=inl_board)
    
@router.message(F.text.lower() == "английский язык")
async def english(message: types.Message):
    await message.reply("""🌍 Английский язык\n
Возраст: 7–14 лет\n
Длительность: 6 месяц\n
Разговорная практика, словарный запас, грамматика и понимание на слух.""", reply_markup=inl_board)
    
@router.message(F.text.lower() == "контакты")
async def contacts(message: types.Message):
    await message.answer(
        "🕒 Пн-Сб 09:00–19:00\nПиши администратору: @admin"
    )
    await message.answer_contact(
        phone_number='+996555123456',
        first_name='Mogutova',
        last_name='Miraida'
    )
    
@router.message(F.text.lower() == 'адрес')
async def adress(message: types.Message):
    await message.answer("г. Ош, ул. Курманжан Датка, 213")
    await message.answer_location(
        latitude=40.50967731331906,
        longitude=72.8099170274063
    )


@router.callback_query(F.data == 'confirm')
async def callback_confirm(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "номер адимистратора: +996555 123 456"
    )
    await callback.answer()

@router.callback_query(F.data == "cancel")
async def cancel(callback: types.CallbackQuery):
    await callback.message.answer(
        "Вернулось в главное меню", reply_markup=classic_board
    )
    await callback.answer()
