from aiogram import Router
from aiogram.filters import CommandStart  
from aiogram import types, F 
from replyinline import reply_keyboard, inline_keyboard

router = Router()

@router.message(CommandStart())
async def inline_start(message: types.Message):
    await message.answer(
        "Привет!Добро пожаловать в наш телеграм бот!",
        reply_markup=reply_keyboard
    )

@router.message(F.text == "Показать текст")     
async def show_text(message: types.Message):    
    await message.reply(                        
        "Ты хочешь очистить экран?",            
        reply_markup=inline_keyboard
    )

@router.message(F.text == "Очистить экран")     
async def ask_clear(message: types.Message):    
    await message.reply(                        
        "Ты уверен?",                           
        reply_markup=inline_keyboard       
    )

@router.callback_query(F.data == "confirm")     
async def callback_confirm(callback: types.CallbackQuery):  
    await callback.message.edit_text(
        "Экран очищен!"                       
    )
    await callback.answer()                     

@router.callback_query(F.data == "cancel")       
async def callback_cancel(callback: types.CallbackQuery):
    await callback.message.edit_text(            
        "Действие отменяется"                  
    )
    await callback.answer()                  
