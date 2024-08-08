from aiogram import Dispatcher, types
from config import bot
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def quizzz(message: types.Message):
    buttom_quiz = InlineKeyboardMarkup()
    buttom_quiz_1 =InlineKeyboardButton(text="Дальше!",
                                        callback_data="buttom-1")

    buttom_quiz.add(buttom_quiz_1)

    question = "Чей Крым?"
    answer = ["России", "Украины", "НАШ!"]

    await bot.send_poll(chat_id=message.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type="quiz",
                        correct_option_id=2,
                        explanation="Думай ещё раз",
                        reply_markup=buttom_quiz
                        )


async def quizzz_2(call: types.CallbackQuery):

    await bot.send_photo(chat_id=call.from_user.id,
                         photo=open("media/molodez.png", "rb"))

    buttom_quiz = InlineKeyboardMarkup()
    buttom_quiz_1 =InlineKeyboardButton(text="Дальше!",
                                        callback_data="buttom-2")

    buttom_quiz.add(buttom_quiz_1)

    question = "Какой шутер лучше?"
    answer = ["Fortnight", "CS-2", "CoD", "Free Fire", "PUBG"]

    await bot.send_poll(chat_id=call.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type="quiz",
                        correct_option_id=0,
                        explanation="Позер))",
                        reply_markup=buttom_quiz
                        )


async def quizzz_3(call: types.CallbackQuery):

    buttom_quiz = InlineKeyboardMarkup()
    buttom_quiz_1 =InlineKeyboardButton(text="Дальше!",
                                        callback_data="buttom-3")

    buttom_quiz.add(buttom_quiz_1)

    question = "Тварь ли я дрожашая, или право имею??"
    answer = ["Ты тварь, епта", "Все имеют право", "Фиг его знаеть", "Стоит задуматься"]

    await bot.send_poll(chat_id=call.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type="quiz",
                        correct_option_id=3,
                        explanation="Иди читай, шкильник",
                        reply_markup=buttom_quiz
                        )


async def quizzz_4(call: types.CallbackQuery):
    await bot.send_photo(chat_id=call.from_user.id,
                         photo=open("media/put.png", "rb"))

    question = "Пойдешь на лева - богатым будешь.\nПойдешь на  право - героям станешь.\nПойдешь вперед - смерть тебя ждет!"
    answer = ["Лева", "Вперед", "Право"]

    await bot.send_poll(chat_id=call.from_user.id,
                        question=question,
                        options=answer,
                        is_anonymous=True,
                        type="quiz",
                        correct_option_id=1,
                        explanation="А ловка ты это придумал, молодец",
                        )


def register_quizzz(dp: Dispatcher):
    dp.register_message_handler(quizzz, commands=['quiz'])
    dp.register_callback_query_handler(quizzz_2, text="buttom-1")
    dp.register_callback_query_handler(quizzz_3, text="buttom-2")
    dp.register_callback_query_handler(quizzz_4, text="buttom-3")



# async def sennd_poll(chat_id, question, options, correct_option_id):
#     await bot.send_poll(chat_id=chat_id,
#                         question=question,
#                         options=answer,
#                         is_anonymous=True,
#                         type="quiz",
#                         correct_option_id=3,
#                         explanation="Иди читай, шкильник",
#                         )