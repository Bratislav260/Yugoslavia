import re

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text, state
from aiogram.dispatcher.filters.state import State, StatesGroup
import bottons
from aiogram.types import ReplyKeyboardRemove


class FSM_reg(StatesGroup):
    fullname = State()
    age = State()
    email = State()
    gender = State()
    phone = State()
    photo = State()


async def fsm_start(message: types.Message):
    await message.answer(text="Приветствую \n"
                              "Напишите свое ФИО: \n"
                         "Можете отменить - отмена", reply_markup=bottons.cancel)
    await FSM_reg.fullname.set()


async def load_name(message: types.Message, state: FSMContext):
    await loading(message, state, "fullname")
    # async with state.proxy() as data:
    #     data['fullname'] = message.text
    # await FSM_reg.next()

    await message.answer(text="Укажите свой возвраст: ")


async def load_age(message: types.Message, state: FSMContext):
    await loading(message, state, "email")
    # async with state.proxy() as data:
    #     data['age'] = message.text
    # await FSM_reg.next()

    await message.answer(text="Укажите свою почту: ")


async def load_email(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        email = message.text.strip()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            await message.answer("")
            return
        data['email'] = message.text

    await FSM_reg.next()
    await message.answer(text="Укажите свой пол: ")


async def load_gender(message: types.Message, state: FSMContext):
    await loading(message, state, "gender")
    # async with state.proxy() as data:
    #     data['gender'] = message.text
    # await FSM_reg.next()

    await message.answer(text="Укажите свой телефон: ")


async def load_phone(message: types.Message, state: FSMContext):
    await loading(message, state, "phone")
    # async with state.proxy() as data:
    #     data['phone'] = message.text


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text="Отмена")


async def loading(message: types.Message, state: FSMContext, name):
    async with state.proxy() as data:
        data[name] = message.text
    await FSM_reg.next()


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data["photo"] = message.photo[-1].file_id

    kb = types.ReplyKeyboardMarkup()

    await message.answer_photo(photo=data['photo'],
                               caption=f"{data['fullname']}\n"
                                       f"{data['age']}\n"
                                       f"{data['email']}\n"
                                       f"{data['gender']}\n"
                                       f"{data['phone']}\n")
    await message.answer("Спасибо за регистрацию", reply_markup=kb)
    await state.finish()


def register_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals="отмена", ignore_case=True), state="*")
    dp.register_message_handler(fsm_start, commands="reg")
    dp.register_message_handler(load_name, state=FSM_reg.fullname)
    dp.register_message_handler(load_age, state=FSM_reg.age)
    dp.register_message_handler(load_email, state=FSM_reg.email)
    dp.register_message_handler(load_gender, state=FSM_reg.gender)
    dp.register_message_handler(load_phone, state=FSM_reg.phone)

