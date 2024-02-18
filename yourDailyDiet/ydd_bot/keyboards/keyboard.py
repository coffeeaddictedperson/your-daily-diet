import os

from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, LoginUrl, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from messages import BUTTONS, USER_NOT_FOUND, LOGGED_USER

GET_YOUR_MEAL = 'Get your meal'
SHARE_PHONE_TO_LOGIN = 'Share phone to login'
SHARE_PHONE_TO_SIGNUP = 'Share phone to signup'

request_url = os.getenv('SERVER_ROUTE')
signup_route = f'{request_url}/signup/'
login_route = f'{request_url}/login/'


def get_keyboard(message: Message = None):
    user_id = message.from_user.id
    username = message.from_user.username

    # Check if user id exist in the database
    # Yes - check last time logged in
    # if more the 24 hours - return keyboard with login
    # return keyboard with get_your_meal
    # No - return keyboard with sign_up

    # return ReplyKeyboardMarkup(
    #     keyboard=[[
    #         KeyboardButton(text=BUTTONS['get_your_meal']),
    #     ]])

    signup_url = LoginUrl(
        url=f'{signup_route}?username={username}&userid={user_id}',
        bot_username='@YourDailyDietAssistantBot',
    )

    login_url = LoginUrl(
        url=f'{login_route}?username={username}&userid={user_id}',
        bot_username='@YourDailyDietAssistantBot',
    )

    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=BUTTONS['sign_up'], login_url=signup_url),
        InlineKeyboardButton(text=BUTTONS['login'], login_url=login_url),
    )
    builder.row(
        InlineKeyboardButton(text=BUTTONS['verify'],
                             callback_data='verify'),
    )
    return builder.as_markup()


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
