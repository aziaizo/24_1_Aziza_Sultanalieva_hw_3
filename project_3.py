from aiogram.utils import executor
from hendlers import callback,client,admin
import logging
from config import disp


client.register_hendlers_client(disp)
callback.register_hendlers_callback(disp)
admin.register_handlers_admin(disp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(disp,skip_updates=True)