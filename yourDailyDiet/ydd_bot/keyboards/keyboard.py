import os

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, LoginUrl)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from messages import BUTTONS, USER_NOT_FOUND, LOGGED_USER

GET_YOUR_MEAL = 'Get your meal'
SHARE_PHONE_TO_LOGIN = 'Share phone to login'
SHARE_PHONE_TO_SIGNUP = 'Share phone to signup'

request_url = os.getenv('SERVER_ROUTE')
login_view_route = 'https://127.0.0.1/login/'


def get_keyboard(state=None):
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text=BUTTONS['get_your_meal']),
        ]])



    # This part requires real domain. was not be able to test it locally,
    # skipped
    # if state == USER_NOT_FOUND:
    #     return ReplyKeyboardMarkup(
    #         keyboard=[[
    #             KeyboardButton(text=BUTTONS['sign_up']),
    #             KeyboardButton(text=BUTTONS['cancel'])
    #         ]])
    # elif state == LOGGED_USER:
    #     return ReplyKeyboardMarkup(
    #         keyboard=[[
    #             KeyboardButton(text=BUTTONS['get_your_meal']),
    #             KeyboardButton(text=BUTTONS['logout'])
    #         ]])
    #
    # login_url = LoginUrl(
    #     url=login_view_route,
    #     forward_text='forward_text',
    #     bot_username='@YourDailyDietAssistantBot',
    #     # request_write_access: Optional[bool] = None,
    # )
    #
    # builder = InlineKeyboardBuilder()
    # builder.add(
    #     InlineKeyboardButton(text=BUTTONS['login'], login_url=login_url))
    # return builder.as_markup()
