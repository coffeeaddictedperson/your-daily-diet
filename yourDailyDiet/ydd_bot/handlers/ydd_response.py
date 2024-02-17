from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter

from handlers.call_api import get_meal_types, get_random_meal
from handlers.call_user_api import BotUser

from messages import (WELCOME_MESSAGE, UNKNOWN_COMMAND_MESSAGE,
                      MESSAGES, LOGGED_USER, USER_NOT_FOUND, USER_ALREADY_EXIST)
from keyboards.inline_keyboard import get_meal_types_keyboard, YDDCallback
from keyboards.keyboard import get_keyboard, GET_YOUR_MEAL

router = Router()

# Start command, private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    FormattedCommandFilter(['/start', '/cancel']),
)
async def process_start_command(message: Message):
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=get_keyboard()
    )


# # Login user
# # @private channel only,
# # @accept "/login", "login" (case in-sensitive)
# @router.message(
#     ChatTypeFilter(chat_type=["private"]),
#     FormattedCommandFilter(['/login']),
# )
# async def process_login_command(message: Message):
#     print('Private chat: received /login command')
#     status = await BotUser.verify_user_id(message)
#
#     if status == USER_NOT_FOUND:
#         await message.answer(
#             MESSAGES['user_not_found'],
#             reply_markup=get_keyboard(USER_NOT_FOUND)
#         )
#     else:
#         await message.answer(
#             MESSAGES['login_successful'],
#             reply_markup=get_keyboard(LOGGED_USER)
#         )


# # Sign up user
# # @private channel only,
# # @accept "/sign up", "signup" (case in-sensitive)
# @router.message(
#     ChatTypeFilter(chat_type=["private"]),
#     FormattedCommandFilter(['/signup']),
# )
# async def process_signup_command(message: Message):
#     print('Private chat: received /signup command')
#     status = await BotUser.signup_user(message)
#
#     if status == USER_ALREADY_EXIST:
#         await message.answer(
#             MESSAGES['user_not_found'],
#             reply_markup=get_keyboard(USER_NOT_FOUND)
#         )
#     else:
#         await message.answer(
#             MESSAGES['signup_successful'],
#             reply_markup=get_keyboard(LOGGED_USER)
#         )


# Get your meal command, private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    FormattedCommandFilter([GET_YOUR_MEAL]),
)
async def process_echo(message: Message):
    # send request to api to get meal types
    meal_types = await get_meal_types()
    keyboard = get_meal_types_keyboard(meal_types)
    await message.answer(WELCOME_MESSAGE, reply_markup=keyboard)


@router.callback_query(YDDCallback.filter(F.cb_type == "meal_type"))
async def process_ydd_command(query: CallbackQuery, callback_data: YDDCallback):
    try:
        # send request to api to get meal
        meal = await get_random_meal(meal_type=callback_data.value)

        if meal != 'None' and meal is not None:
            await query.message.answer(f'Your meal is {meal}')
        else:
            await query.message.answer(
                f'No meal found for {callback_data.value}')
    except:
        await query.message.answer(f'No meal found for {callback_data.value}. '
                                   f'Try again later.')

# Non of the above commands are matched: show warning message
@router.message()
async def process_echo(message: Message):
    # if message.contact is not None:
    #     # ...
    #     #
    #     # await message.answer(f"You logged in successfully")
    # else:
        await message.answer(UNKNOWN_COMMAND_MESSAGE)
