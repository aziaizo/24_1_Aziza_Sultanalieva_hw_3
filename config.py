from aiogram import Bot, Dispatcher
from decouple import config


TOKEN=config("TOKEN")
bot=Bot(TOKEN)
disp=Dispatcher(bot=bot)
ADMINS=[800798702,787262263]