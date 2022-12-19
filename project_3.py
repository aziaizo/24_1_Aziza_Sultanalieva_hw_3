from aiogram.utils import executor
from hendlers import callback,client,admin,fsmAdminMentor
import logging
from config import disp

fsmAdminMentor.register_handlers_fsm_admin_mentor(disp)
client.register_hendlers_client(disp)
callback.register_hendlers_callback(disp)
admin.register_handlers_admin(disp)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(disp,skip_updates=True)