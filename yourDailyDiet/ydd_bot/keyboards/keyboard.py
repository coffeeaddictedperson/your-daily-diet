from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

GET_YOUR_MEAL = 'Get your meal'


def get_keyboard():
    return (ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text=GET_YOUR_MEAL)]],
    ))
