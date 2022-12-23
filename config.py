from aiogram import Bot, Dispatcher
from decouple import config
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage=MemoryStorage()


TOKEN=config("TOKEN")
bot=Bot(TOKEN)
disp=Dispatcher(bot=bot, storage=storage)
ADMINS=[800798702,787262263]