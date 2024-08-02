from aiogram import Dispatcher, types
from config import bot
import os
from aiogram.types import InputFile
from random import *


#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Хой, я Тэмм")
    await message.answer("Тэмм, алергия на Тэмм")


async def info_handler(message: types.Message):
    await message.answer("Это бот, имитирующий Темми из игры 'Undertale'")


async def meme_handler(message: types.Message):
    path = "media/"
    files = []

    for i in os.listdir(path):
        full_path = os.path.join(path, i)

        if os.path.isfile(full_path):
            files.append(full_path)

    random_meme = choice(files)
    await message.answer_photo(photo=InputFile(random_meme))


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(meme_handler, commands=['meme', 'photo'])
