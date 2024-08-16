import logging
from aiogram.contrib.middlewares import fsm
from config import dp, bot
from aiogram.utils import executor
from handlers import commands, massage, quizzz, game, FSM_reg, FSN_online_store
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
FSM_reg.register_fsm(dp)
FSN_online_store.register_fsn_store(dp)

massage.register_massage(dp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)
