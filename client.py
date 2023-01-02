from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot,disp
from database.bot_db import sql_command_random
from parser_.serials import ParserSerials


async def start(message: types.Message):
    await bot.send_message(message.from_user.id,text=f'Hi {message.from_user.first_name}')



@disp.message_handler(commands=['quiz'])
async def quiz(message: types.Message):
    markup= InlineKeyboardMarkup()
    button=InlineKeyboardButton("NEXT",callback_data='button')
    markup.add(button)
    question="Решите задачку\n '34+2*5'"
    answers=[
        '180',
        '44',
        '54',
        '170',
    ]
    await bot.send_poll(
        chat_id=message.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation='34+2*5=34+10=44!!',
        reply_markup=markup,
    )


@disp.message_handler(commands=['mem'])
async def mem(message: types.Message):
    photo=open("media/mem.jpg",'rb')
    await bot.send_photo(message.from_user.id, photo=photo)



async def pin(message:types.Message):
    if message.chat.type != "private":
        if not message.reply_to_message:
            await message.answer('Команда должна быть ответом на сообщение')
        else:
             await bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
    else:
        await message.answer('Нужно писать в группе')



async def dice(message: types.Message):
    if message.chat.type != "private":
        await bot.send_message(message.chat.id, text="БОТ")
        a=await bot.send_dice(message.chat.id)
        await bot.send_message(message.chat.id, text=f'{message.from_user.full_name}')
        b=await bot.send_dice(message.chat.id)
        if a.dice.value>b.dice.value:
            await message.answer('Победил SIMUS!')
        elif a.dice.value<b.dice.value:
            await message.answer(f'Победил {message.from_user.full_name}!')
        else:
            await message.answer('Ничья!Победила дружба!')
    else:
        await message.answer('Нужно писать в группе')

async def get_random_user(message: types.Message):
    await sql_command_random(message)



async def get_top_serials(message:types.Message):
    serial=ParserSerials.parser()
    for i in serial:
        await message.answer(
                    f"{i['link']}\n\n"
                    f"{i['title']}\n"
                    f"#{i['type']}\n"
                    f"#{i['genre']}\n"
                )

async def get_top_ten_serials(message:types.Message):
    serial=ParserSerials.parser()
    a=0
    for i in serial:
        if a < 10:
            await message.answer(
                    f"{i['link']}\n\n"
                    f"{i['title']}\n"
                    f"#{i['type']}\n"
                    f"#{i['genre']}\n"
                )
            a+=1



def register_hendlers_client(disp:Dispatcher):
    disp.register_message_handler(start, commands=['start'])
    disp.register_message_handler(quiz, commands=['quiz'])
    disp.register_message_handler(mem, commands=['mem'])
    disp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    disp.register_message_handler(dice, commands=['dice'])
    disp.register_message_handler(get_random_user, commands=['get'])
    disp.register_message_handler(get_top_serials, commands=['serials'])
    disp.register_message_handler(get_top_ten_serials, commands=['top10'])