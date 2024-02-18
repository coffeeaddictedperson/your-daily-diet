
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from messages import GET_YOUR_MEAL


def get_meal_keyboard():
    return ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text=GET_YOUR_MEAL)]])
