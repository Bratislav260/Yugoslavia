from aiogram import Dispatcher, types


# async def echo(message: types.Message):
#     await message.answer(message.text)


async def message_handler(message: types.Message):
    if message.text.isdigit():
        res = int(message.text) ** 2
        await message.answer(res)
    else:
        await message.answer(message.text)


def register_massage(dp: Dispatcher):
    # dp.register_message_handler(echo)
    dp.register_message_handler(message_handler)
