from aiogram import types, Dispatcher
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from config import dp, bot


async def webapp_reply_button(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    stopgame = KeyboardButton("Stop Game",
                                  web_app=types.WebAppInfo(url="https://stopgame.ru"))
    ixbt = KeyboardButton("IXBT Games",
                                  web_app=types.WebAppInfo(url="https://ixbt.games"))
    igromania = KeyboardButton("Igromania",
                                  web_app=types.WebAppInfo(url="https://www.igromania.ru"))
    ign = KeyboardButton("IGN",
                             web_app=types.WebAppInfo(url="https://www.ign.com"))
    playgroud = KeyboardButton("Playgraud",
                             web_app=types.WebAppInfo(url="https://www.playground.ru"))

    keyboard.add(stopgame, ixbt, igromania, ign, playgroud)

    await message.answer(text='Нажми на кнопки для открытия сайтов', reply_markup=keyboard)


async def webapp_inline_button(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1, resize_keyboard=True)

    stopgame = InlineKeyboardButton("Stop Game",
                                        web_app=types.WebAppInfo(url="https://stopgame.ru"))
    ixbt = InlineKeyboardButton("IXBT Games",
                                        web_app=types.WebAppInfo(url="https://ixbt.games"))
    igromania = InlineKeyboardButton("Igromania",
                                        web_app=types.WebAppInfo(url="https://www.igromania.ru"))
    ign = InlineKeyboardButton("IGN",
                                     web_app=types.WebAppInfo(url="https://www.ign.com"))
    playgroud = InlineKeyboardButton("Playgraud",
                                     web_app=types.WebAppInfo(url="https://www.playground.ru"))

    keyboard.add(stopgame, ixbt, igromania, ign, playgroud)

    await message.answer(text='Нажми на кнопки для открытия сайтов', reply_markup=keyboard)


async def pin_message(message: types.Message):
    if message.chat.type != "private":
        if message.reply_to_message:
            await bot.pin_chat_message(chat_id=message.chat.id, message_id=message.reply_to_message.message_id)
        else:
            await message.answer("Команда должен быть ответом, чтобы закрепили!")
    else:
        await message.answer("Команда работает только в группе!")


def register_webapp_handlers(dispatcher: Dispatcher):
    dp.register_message_handler(webapp_reply_button, commands=['webapp'])
    dp.register_message_handler(pin_message, text='!pin')
    dp.register_message_handler(webapp_inline_button, commands=['webappLine'])
