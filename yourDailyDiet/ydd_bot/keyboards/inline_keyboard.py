from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from messages import BTN_BREAKFAST, BTN_SNACK, BTN_DINNER

btn_breakfast = KeyboardButton(text=BTN_BREAKFAST)

btn_snack = KeyboardButton(text=BTN_SNACK)

btn_dinner = KeyboardButton(text=BTN_DINNER)

kb = ReplyKeyboardMarkup(keyboard=[[btn_breakfast, btn_snack, btn_dinner]],
                         resize_keyboard=True,
                         one_time_keyboard=False)
