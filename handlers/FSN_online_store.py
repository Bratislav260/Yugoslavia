# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Text, state
# from aiogram.dispatcher.filters.state import State, StatesGroup
# import bottons
# from handlers import FSM_reg
#
#
# class fsn_store(StatesGroup):
#     pro_name = State()
#     pro_size = State()
#     pro_category = State()
#     pro_price = State()
#     pro_photo = State()
#     pro_id = State()
#     submit = State()
#
#
# async def fsn_start(message: types.Message):
#     await fsn_store.pro_name.set()
#     await message.answer("text='Введите название товара: ", reply_markup=bottons.cancel)
#
#
# async def load_pro_name(message: types.Message, state: FSMContext):
#     await load_pro(message, state, "pro_name")
#     await message.answer(text="Укажите размер товара: ", reply_markup=bottons.sizes)
#
#
# async def load_pro_size(message: types.Message, state: FSMContext):
#     await load_pro(message, state, "pro_size")
#     await message.answer(text="Укажите категорию товара: ")
#
#
# async def load_pro_category(message: types.Message, state: FSMContext):
#     await load_pro(message, state, "pro_category")
#     await message.answer(text="Укажите цену товара: ")
#
#
# async def load_pro_price(message: types.Message, state: FSMContext):
#     await load_pro(message, state, "pro_price")
#     await message.answer(text="Укажите артикул товара: ")
#
#
# async def load_pro_id(message: types.Message, state: FSMContext):
#     await load_pro(message, state, "pro_id")
#     await message.answer(text="Укажите фото товара: ")
#
#
# async def load_pro_photo(message: types.Message, state: FSMContext):
#     await load_pro(message, state, "pro_photo")
#     await message.answer(text="Укажите свой телефон: ", reply_markup=bottons.submit)
#
#
# async def summit(message: types.Message, state: FSMContext):
#     kb = types.ReplyKeyboardMarkup()
#     if message.text == "Да":
#         await message.answer("Данные сохранины", reply_markup=kb)
#         await state.finish()
#     elif message.text == "Нет":
#         await message.answer("Отменено!", reply_markup=kb)
#         await state.finish()
#
#
# async def load_pro(message: types.Message, state: FSMContext, name):
#     async with state.proxy() as data_store:
#         data_store[name] = message.text
#     await fsn_store.next()
#
#
# def register_fsn_store(dp: Dispatcher):
#     dp.register_message_handler(FSM_reg.cancel_fsm, Text(equals="отмена", ignore_case=True), state="*")
#     dp.register_message_handler(fsn_start, commands="pro")
#     dp.register_message_handler(load_pro_name, state=fsn_store.pro_name)
#     dp.register_message_handler(load_pro_size, state=fsn_store.pro_size)
#     dp.register_message_handler(load_pro_category, state=fsn_store.pro_category)
#     dp.register_message_handler(load_pro_price, state=fsn_store.pro_price)
#     dp.register_message_handler(load_pro_id, state=fsn_store.pro_id)
#     dp.register_message_handler(load_pro_photo, state=fsn_store.pro_photo)

from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import bottons
from aiogram.dispatcher.filters.state import State, StatesGroup


class FSM_store(StatesGroup):
    name_product = State()
    size_product = State()
    price_product = State()
    id_product = State()
    photo_product = State()
    submit = State()


async def fsm_start(message: types.Message):
    await FSM_store.name_product.set()
    await message.answer(text='Введите название товара: ',
                         reply_markup=bottons.cancel)


async def load_name_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['name_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите размер товара: ')


async def load_size_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['size_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите цену товара: ')


async def load_price_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['price_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Укажите артикул товара: ')


async def load_id_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['id_product'] = message.text

    await FSM_store.next()
    await message.answer(text='Отправьте фотографию товара:')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data_store:
        data_store['photo'] = message.photo[-1].file_id

    await message.answer_photo(photo=data_store['photo'],
                               caption=f"Название товара - {data_store['name_product']}\n"
                                       f"Размер - {data_store['size_product']}\n"
                                       f"Цена - {data_store['price_product']}\n"
                                       f"Артикул - {data_store['id_product']}",
                               reply_markup=bottons.submit)
    await FSM_store.next()


async def submit(message: types.Message, state: FSMContext):
    if message.text == "Да":
        kb = types.ReplyKeyboardRemove()
        await message.answer(text='Ваши данные сохранены!', reply_markup=kb)
        await state.finish()
    else:
        await message.answer(text='Отменено!')
        await state.finish()


async def cancel_fsm(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()
        await message.answer(text='Отменено!')


def store_fsm(dp: Dispatcher):
    dp.register_message_handler(cancel_fsm, Text(equals='Отмена',
                                                 ignore_case=True),
                                state="*")

    dp.register_message_handler(fsm_start, commands=['product'])
    dp.register_message_handler(load_name_product, state=FSM_store.name_product)
    dp.register_message_handler(load_size_product, state=FSM_store.size_product)
    dp.register_message_handler(load_price_product, state=FSM_store.price_product)
    dp.register_message_handler(load_id_product, state=FSM_store.id_product)
    dp.register_message_handler(load_photo, state=FSM_store.photo_product, content_types=['photo'])
    dp.register_message_handler(submit, state=FSM_store.submit)
