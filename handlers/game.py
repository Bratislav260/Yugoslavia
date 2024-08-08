from aiogram import Dispatcher, types
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


user_score = 0
bot_score = 0


async def bowling_game(call: types.CallbackQuery): #сама игра
    global user_score, bot_score

    emo_user = await bot.send_dice(chat_id=call.from_user.id, emoji="🎳")
    await bot.send_message(chat_id=call.from_user.id, text="Игрок: " + str(emo_user.dice.value))
    emo_bot = await bot.send_dice(chat_id=call.from_user.id, emoji="🎳")
    await bot.send_message(chat_id=call.from_user.id, text="Тэмм_бот: " + str(emo_bot.dice.value))

    if emo_bot.dice.value > emo_user.dice.value:
        bot_score += 1
    else:
        user_score += 1

    await bot.send_message(chat_id=call.from_user.id, text=f"Тэмм_бот: {emo_bot.dice.value}, Игрок: {emo_user.dice.value},\nСчёт: {bot_score}:{user_score}")

    await menu_game("Хотите продолжить?", call.from_user.id)


async def menu_game(string, chat_id): #Реализация интерфейса
    button_game = InlineKeyboardMarkup(row_width=2)
    button_game_1 = InlineKeyboardButton(text="Да",
                                         callback_data="button-1")
    button_game_2 = InlineKeyboardButton(text="Нет",
                                         callback_data="button-2")

    button_game.add(button_game_1, button_game_2)
    await bot.send_message(chat_id=chat_id, text=string, reply_markup=button_game)


async def exit_game(call: types.CallbackQuery):
    global user_score, bot_score
    user_score = 0
    bot_score = 0

    await bot.send_message(chat_id=call.from_user.id, text="Спасибо за игру!")


async def interface_game(message: types.Message):
    await menu_game("Хотите сыграть со мной боулинг?", message.from_user.id)


def register_game(dp: Dispatcher):
    dp.register_message_handler(interface_game, commands=['game'])
    dp.register_callback_query_handler(bowling_game, text="button-1")
    dp.register_callback_query_handler(exit_game, text="button-2")

