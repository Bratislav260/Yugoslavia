import logging
from config import dp
from aiogram.utils import executor
from handlers import commands, massage


commands.register_commands(dp)

massage.register_massage(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
