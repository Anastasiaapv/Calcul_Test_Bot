from aiogram import types
import bot001.view as view
from bot001.bot import bot


async def start(message: types.Message):
    await view.greetings(message)
        
async def finish(message: types.Message):
    await view.bay(message)
        

async def getNumber(message: types.Message):

    await view.input_dat(message)
  