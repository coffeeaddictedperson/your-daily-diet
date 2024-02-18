from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from api.get_user import verify_user_code
from api.get_ydd import get_meal_types
from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter

from handlers.states import VerifyCode

from keyboards.meal_types_keyboard import YDDCallback, get_meal_types_keyboard
from keyboards.auth_keyboard import get_keyboard

from messages import WELCOME_MESSAGE

USER_VERIFIED = "user_verified"
USER_EXPIRED = "user_expired"
USER_NON_VERIFIED = "user_non_verified"
USER_NOT_FOUND = "user_not_found"

GET_MEAL_TYPES_STEP = 'get_meal_types'
GET_MEAL_STEP = 'get_meal'


def get_verification_message(user_status):
    if user_status == USER_VERIFIED:
        return None

    if user_status == USER_EXPIRED:
        message_text = ('Bot verification code is expired. Please get new code '
                        'and verify.')
    elif user_status == USER_NON_VERIFIED:
        message_text = 'Bot code is not verified. Please verify the code.'
    else:
        message_text = 'Bot is not verified. Sign up or login to get the code.'

    return message_text


