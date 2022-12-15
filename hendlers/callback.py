from aiogram import types,Dispatcher
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot,disp



# @disp.callback_query_handler(text="button")
async def quiz2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button2 = InlineKeyboardButton("NEXT", callback_data='button2')
    markup.add(button2)
    question="Сколько штатов в США?"
    answers=[
        '50',
        '51',
        '54',
        '56',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=0,
        explanation='В США 50 штатов!!!',
        reply_markup=markup
    )


# @disp.callback_query_handler(text="button2")
async def quiz3(call: types.CallbackQuery):
    question="Какая планета считается самой холодной в солнечной системе?"
    answers=[
        'Венера',
        'Сатурн',
        'Нептун',
        'Уран',
    ]
    await bot.send_poll(
        chat_id=call.from_user.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation='Температура в Уране составляет -224°С',
    )

def register_hendlers_callback(disp:Dispatcher):
    disp.register_callback_query_handler(quiz2, text="button")
    disp.register_callback_query_handler(quiz3, text="button2")