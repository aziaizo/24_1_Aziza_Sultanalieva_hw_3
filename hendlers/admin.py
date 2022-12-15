from aiogram import types, Dispatcher
from config import bot
from config import ADMINS
from random import choice

async def game (message: types.Message):
    games=['🏀','🎲','⚽','🎯','🎳','🎰']
    game = choice(games)
    if message.text.lower().startswith('game'):
        if message.chat.type != "private":
            if message.from_user.id not in ADMINS:
                await message.answer('Ты не админ!')
            else:
                await bot.send_dice(message.chat.id, emoji=game)

        else:
            await message.answer('Пиши в группу')


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game)