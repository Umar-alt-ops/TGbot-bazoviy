from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

command = [BotCommand(command="start", description='Начать')]

replybuttons = [                                      
    [KeyboardButton(text="Показать текст")],     
    [KeyboardButton(text="Очистить экран")],    
]
reply_keyboard = ReplyKeyboardMarkup(                  
    keyboard=replybuttons,                            
    resize_keyboard=True                         
)

inlinebuttons = [                          
    [InlineKeyboardButton(text="Да", callback_data="confirm")],   
    [InlineKeyboardButton(text="Нет", callback_data="cancel")],  
]

inline_keyboard = InlineKeyboardMarkup(         
    inline_keyboard=inlinebuttons             
)
