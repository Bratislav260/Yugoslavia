from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

cancel = ReplyKeyboardMarkup(resize_keyboard=True).add(
    KeyboardButton("Отмена"))

buttons_row = [KeyboardButton("S"), KeyboardButton("M"), KeyboardButton("L"), KeyboardButton("XL"),
               KeyboardButton("XXL"), KeyboardButton("XXXL")]

sizes = ReplyKeyboardMarkup(keyboard=[buttons_row], resize_keyboard=True)
submit = ReplyKeyboardMarkup(keyboard=[[KeyboardButton("Да"), KeyboardButton("Нет")]], resize_keyboard=True)