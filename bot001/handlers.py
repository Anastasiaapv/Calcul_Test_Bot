from aiogram import Dispatcher

import bot001.commands as commands

def registed_handlers(dp: Dispatcher):
    dp.register_message_handler (commands.start, commands=['start']) 
    dp.register_message_handler (commands.finish, commands=['finish']) 
    dp.register_message_handler (commands.getNumber)