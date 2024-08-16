# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text, state
# from aiogram.dispatcher.filters.state import State, StatesGroup
# import FSM_reg
# import bottons


# class FSM_store(StatesGroup):
#     pro_name = State()
#     size = State()
#     category = State()
#     price = State()
#     photo = State()
#
#
# async def store_start(message: types.Message):
#     await message.answer(text="Приветствую \n"
#                               "Напишите имя товара: \n"
#                          "Можете отменить - отмена", reply_markup=bottons.cancel)
#     await FSM_store.pro_name.set()
#
#
# async def name(message: types.Message, state: FSMContext):
#     await FSM_reg.loading(message, state, "pro_name")
#     await message.answer(text="Укажите размер(X, XL, XXL, XXXL): ", reply_markup=bottons.sizes)
#
#
# async def size(message: types.Message, state: FSMContext):
#     await FSM_reg.loading(message, state, "size")
#     await message.answer(text="Укажите категорию: ")
#
#
# async def category(message: types.Message, state: FSMContext):
#     await FSM_reg.loading(message, state, "category")
#     await message.answer(text="Укажите цену: ")
#
#
# async def price(message: types.Message, state: FSMContext):
#     await FSM_reg.loading(message, state, "price")
#     await message.answer(text="Отправьте фото товара: ")
#
#
# async def photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data["photo"] = message.photo[-1].file_id
#
#     kb = types.ReplyKeyboardMarkup()
#
#     await message.answer_photo(photo=data['photo'],
#                                caption=f"{data['pro_name']}\n"
#                                        f"{data['size']}\n"
#                                        f"{data['category']}\n"
#                                        f"{data['price']}\n"
#                                        f"{data['phone']}\n")
#     await message.answer("", reply_markup=kb)
#     await message.answer("Верные ли данные?", reply_markup=bottons.answer)
#     await state.finish()
#
#
# async def store_net(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is not None:
#         await state.finish()
#         await message.answer(text="Нет")
#
#
# async def store_da(message: types.Message, state: FSMContext):
#     current_state = await state.get_state()
#     if current_state is not None:
#         await state.finish()
#         await message.answer(text="Да")
#         await message.answer(text="Сохранено в базу")
#
#
# def register_fsm_store(dp: Dispatcher):
#     dp.register_message_handler(FSM_reg.cancel_fsm, Text(equals="отмена", ignore_case=True), state="*")
#     dp.register_message_handler(store_net, Text(equals="нет", ignore_case=True), state="*")
#     dp.register_message_handler(store_da, Text(equals="да", ignore_case=True), state="*")
#     dp.register_message_handler(store_start, commands="store")
#     dp.register_message_handler(name, state=FSM_store.pro_name)
#     dp.register_message_handler(size, state=FSM_store.size)
#     dp.register_message_handler(category, state=FSM_store.category)
#     dp.register_message_handler(price, state=FSM_store.price)
#     dp.register_message_handler(photo, state=FSM_store.photo)
