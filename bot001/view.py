from aiogram import types
from bot001.bot import bot

async def greetings(message: types.Message):
    await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, приветик!\n'
        f'Я калькулятор. Введи свой пример\n')

async def bay(message: types.Message):
    await bot.send_message(message.from_user.id,
        f'{message.from_user.first_name}, пока!\n'
        f'Захочешь ещё посчитать - возвращайся!\n')

async def input_dat(message: types.Message):
    number = message.text
    while True:
        await bot.send_message(message.from_user.id,f'Ответ: {eval(number)}')
        break

