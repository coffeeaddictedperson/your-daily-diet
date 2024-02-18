import os

from aiogram.types import (InlineKeyboardButton, LoginUrl, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder

from keyboards.callback_data import YDDCallback
from messages import BUTTONS

request_url = os.getenv('SERVER_ROUTE')
signup_route = f'{request_url}/signup/'
login_route = f'{request_url}/login/'



def get_keyboard(message: Message = None):
    user_id = message.chat.id
    username = message.chat.username

    print('*'*10)
    print(user_id, username, message)

    signup_url = LoginUrl(
        url=f'{signup_route}?username={username}&userid={user_id}',
        bot_username='@YourDailyDietAssistantBot',
    )

    login_url = LoginUrl(
        url=f'{login_route}?username={username}&userid={user_id}',
        bot_username='@YourDailyDietAssistantBot',
    )
    callback_data = YDDCallback(
        cb_type="verify_code",
        value="verify"
    ).pack()

    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text=BUTTONS['sign_up'], login_url=signup_url),
        InlineKeyboardButton(text=BUTTONS['login'], login_url=login_url),
    )
    builder.row(
        InlineKeyboardButton(text=BUTTONS['verify'],
                             callback_data=callback_data)
    )
    return builder.as_markup()
