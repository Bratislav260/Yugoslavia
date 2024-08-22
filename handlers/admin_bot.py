import time

from aiogram import types, Dispatcher
from config import admin, bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
import logging


async def welcome_user(message: types.Message):
    for member in message.new_chat_members:
        await message.answer(f"Добро пожаловать, {member.full_name}\n\n"
                             f"Правила группы:\n"
                             f"Не спамить\n"
                             f"Не токсичить")

words = ['дурак', 'кретин', 'тип', 'чорт']
pre = ['1', '🟩 - 1', '🟨 - 2', '🟥 - 3']
users_pre = {}


async def filter_words(message: types.Message): # добавлен способ подсчета кол-во нарушении
    message.text = message.text.lower()
    for word in words:
        if word in message.text:
            await message.answer(f"Не ругайся!\nПридуприждаем, после 3 трех нарушении ты быдешь забанен! {pre[1]}")
            await check_pre(message)
            if users_pre[message.from_user.id] == 3:
                await message.answer(f"Пользователь {message.from_user.first_name} "
                                     f"забанен за нарушении правил сообщество!")
            await message.delete()
            break


async def check_pre(message: types.Message): # проверка кол-во нарушении
    if message.from_user.id not in users_pre:
        users_pre[message.from_user.id] = 1
    else:
        users_pre[message.from_user.id] += 1


async def delete_user(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in admin:
            await message.answer("Ты не админ!")
        elif message.reply_to_message:
            await message.answer("Команда должен быть ответом на сообщение!")
        else:
            user_id = message.from_user.id
            user_name = message.from_user.first_name
            await message.answer(f"Вы действительно хотите удалить {user_name}",
                                 reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
                            f"Удалить", callback_data=f"delete {user_id}")))
    else:
        await message.answer("Это команда должна быть использовано в группе")


async def complete_delete_user(call: types.CallbackQuery):
    user_id = int(call.data.replace("delete_user ", ""))
    try:
        ban_duration = 3600  # 1 час
        until_date = int(time.time()) + ban_duration # бан на время
        await bot.kick_chat_member(call.message.chat.id, user_id, until_date)
        await bot.unban_chat_member(call.message.chat.id, user_id)
        await call.answer(text='Пользователь удален!', show_alert=True)
        await bot.delete_messages(call.message.chat.id, call.message_id)
    except Exception as e:
        logging.error(f'Error in complete_delete_user: {e}')
        await call.answer(text='Не удалось удалить пользователя', show_alert=True)


def register_admin(dp: Dispatcher):
    dp.register_message_handler(delete_user, commands=["delete"])
    dp.register_message_handler(complete_delete_user,
                                lambda call: call.data and call.data.startwith('delete_user '))
    dp.register_message_handler(filter_words)
    dp.register_message_handler(welcome_user, content_types=[types.ContentType.NEW_CHAT_MEMBERS])
