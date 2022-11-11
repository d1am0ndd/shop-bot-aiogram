from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


#@dp.message_handler(commands=['start', 'help'])
async def command_start(message : types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Разработчик бота: @d1am0ndd', reply_markup=kb_client)
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему:\n@*****')

#@dp.message_handler(commands=['Расположение'])
async def vape_place_command(message : types.Message):
    await bot.send_message(message.from_user.id, '"Город"')

#@dp.message_handler(commands=['Товар'])
async def vape_staff_command(message : types.Message):
    await sqlite_db.sql_read(message)

#@dp.message_handler(commands=['Поддержка'])
async def vape_admin_command(message : types.Message):
    await bot.send_message(message.from_user.id, 'Админ: @*****')

def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(vape_place_command, text=['Расположение'])
    dp.register_message_handler(vape_staff_command, text=['Товар'])
    dp.register_message_handler(vape_admin_command, text=['Поддержка'])
