from aiogram.utils import executor

import bot001.handlers as handlers 
from bot001.bot import dp 

async def on_startup(_):
    print ('Бот работает')

handlers.registed_handlers (dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
