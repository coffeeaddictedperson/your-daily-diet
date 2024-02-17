from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from messages import BUTTONS, USER_NOT_FOUND, LOGGED_USER

GET_YOUR_MEAL = 'Get your meal'
SHARE_PHONE_TO_LOGIN = 'Share phone to login'
SHARE_PHONE_TO_SIGNUP = 'Share phone to signup'


def get_keyboard(state=None):
    if state == USER_NOT_FOUND:
        return ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text=BUTTONS['sign_up']),
                KeyboardButton(text=BUTTONS['cancel'])
            ]])
    elif state == LOGGED_USER:
        return ReplyKeyboardMarkup(
            keyboard=[[
                KeyboardButton(text=BUTTONS['get_your_meal']),
                KeyboardButton(text=BUTTONS['logout'])
            ]])

    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text=BUTTONS['login'], callback_data="random_value"))
    return builder.as_markup()
