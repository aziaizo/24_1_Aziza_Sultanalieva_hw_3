from aiogram import types, Dispatcher
from config import bot, ADMINS
from random import choice
from database.bot_db import sql_command_delete, sql_command_all
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
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


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINS:
        await message.answer("Ты не админ")
    else:
        users=await sql_command_all()
        for user in users:
            await message.answer(f" Имя:{user[1]}\n Направление:{user[2]}"
                                     f" \n Возраст:{user[3]}\n Группа: {user[4]}",
                                 reply_markup=InlineKeyboardMarkup().add(
                                     InlineKeyboardButton(f"delete {user[1]}",
                                                          callback_data=f"delete {user[0]}")
                                 )
                                 )

async def complete_delete(call:types.callback_query):
    await sql_command_delete(call.data.replace('delete', ""))
    await call.answer(text='DELETE',show_alert=True)
    await bot.delete_message(call.from_user.id,call.message.message_id)



def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(game)
    dp.register_message_handler(delete_data,commands=['del'])
    dp.register_callback_query_handler(complete_delete,
                                       lambda call: call.data and call.data.startswith("delete "))