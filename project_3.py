from aiogram.utils import executor
from hendlers import callback,client,admin,fsmAdminMentor
import logging
from config import disp
from database.bot_db import sql_create

fsmAdminMentor.register_handlers_fsm_admin_mentor(disp)

client.register_hendlers_client(disp)
admin.register_handlers_admin(disp)
callback.register_hendlers_callback(disp)


async def on_startup(_):
    sql_create()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(disp,skip_updates=True,on_startup=on_startup)