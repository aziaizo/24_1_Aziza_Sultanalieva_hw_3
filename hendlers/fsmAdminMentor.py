from aiogram import types, Dispatcher
from config import bot, ADMINS
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State,StatesGroup
from keyboards import client_kb
from database.bot_db import sql_command_insert

class FSMAdmin(StatesGroup):
    name=State()
    direction=State()
    age=State()
    group=State()
    submit=State()


async def fsm_start(message: types.Message):
     if message.chat.type == "private":
         if message.from_user.id not in ADMINS:
             await message.answer('Ты не админ!')
         else:
            await FSMAdmin.name.set()
            await message.answer('Введите ваше имя',reply_markup=client_kb.cancel_markup)
     else:
         await message.answer('Пиши в личку!')




async def load_name(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['name']=message.text
    await FSMAdmin.next()
    await message.answer('Какое направление?')


async def load_direction(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['direction']=message.text
    await FSMAdmin.next()
    await message.answer('Ваш возраст?')

async def load_age(message: types.Message, state:FSMContext):
    if not message.text.isdigit():
        await message.answer('Пишите только число')
    elif int(message.text)<16 or int(message.text)>90:
        await message.answer('Возрастное ограничение!')
    else:
        async with state.proxy() as data:
            data['age']=message.text
        await FSMAdmin.next()
        await message.answer('Какая группа?')


async def load_group(message: types.Message, state:FSMContext):
    async with state.proxy() as data:
        data['group']=message.text
    await message.answer(f"Имя:{data['name']}\n Направление:{data['direction']}"
                         f" \n Возраст:{data['age']}\n Группа: {data['group']}")
    await FSMAdmin.next()
    await message.answer('Все верно?',reply_markup=client_kb.submit_markup)


async def submit(message: types.Message, state:FSMContext):
    if message.text.lower() == "да":
        await sql_command_insert(state)
        await state.finish()
        await message.answer("Вы зарегистрированы")
    elif message.text.lower() == "нет":
        await state.finish()
        await message.answer("Регистрация отменена")
    else:
        await message.answer("Нажмите либо на да, либо на нет")

async def cansel_fsm(message: types.Message, state: FSMContext):
    current_state= await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer("Регистрация отменена")

def register_handlers_fsm_admin_mentor(disp:Dispatcher):
     disp.register_message_handler(cansel_fsm,state="*", commands=['cancel'])
     disp.register_message_handler(cansel_fsm,Text(equals='cancel',ignore_case=True), state="*")
     disp.register_message_handler(fsm_start, commands=['reg'])
     disp.register_message_handler(load_name, state=FSMAdmin.name)
     disp.register_message_handler(load_direction, state=FSMAdmin.direction)
     disp.register_message_handler(load_age, state=FSMAdmin.age)
     disp.register_message_handler(load_group, state=FSMAdmin.group)
     disp.register_message_handler(submit, state=FSMAdmin.submit)