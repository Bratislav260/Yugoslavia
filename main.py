import logging
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, massage, quizzz, game
from db import db_main

admin = [2112097330]


async def on_startup(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот включен✅")
        await db_main.sql_creat()


async def on_shutdown(_):
    for i in admin:
        await bot.send_message(chat_id=i, text="Бот выключен❌")

commands.register_commands(dp)
quizzz.register_quizzz(dp)
game.register_game(dp)

massage.register_massage(dp)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
