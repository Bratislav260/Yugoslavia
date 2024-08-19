from aiogram import Dispatcher, types
from config import bot
import os
from aiogram.types import InputFile
from random import *


#@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text="Хой, я Тэмм")
    await message.answer_sticker("CAACAgIAAxkBAAEHc25msG_K_5YRMU-tikM3qIn1AT5HPAACEhgAAhAemUi_BAQfVRhL4TUE")


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


async def sender_handler(message: types.Message):
    file = open("files/это файл.txt", "rb")
    await bot.send_document(message.chat.id, file)


def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])
    dp.register_message_handler(meme_handler, commands=['meme'])
    dp.register_message_handler(sender_handler, commands=['file'])


