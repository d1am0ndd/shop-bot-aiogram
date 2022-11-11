from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('Расположение')
b2 = KeyboardButton('Товар')
b3 = KeyboardButton('Поддержка')

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=None)
kb_client.add(b1).add(b2).add(b3)

