from aiogram import Router, F
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.handlers import CallbackQueryHandler
from aiogram.types import Message, CallbackQuery

from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter

from handlers.call_api import get_meal_types, get_random_meal
from handlers.verify_code import VerifyCode

from messages import WELCOME_MESSAGE
from keyboards.meal_types_keyboard import get_meal_types_keyboard, YDDCallback
from keyboards.auth_keyboard import get_keyboard

router = Router()

# Start command, private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    FormattedCommandFilter(['/start']),
)
async def process_start_command(message: Message):
    print('Private chat: received /start command')
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=get_keyboard(message)
    )


# Verify code command, private channel only
@router.inline_query(YDDCallback.filter(F.cb_type == "verify_code"))
async def process_verify_command(query: CallbackQuery, state: FSMContext):
    print('Private chat: received /verify_code command')
    # await query.message.answer('Enter code:')
    # await state.set_state(VerifyCode.enter_in_verification_mode)
    #
    # await query.message.answer(
    #     "Hi there! What's your name?",
    #     # reply_markup=ReplyKeyboardRemove(),
    # )
# @router.message(VerifyCode.enter_in_verification_mode)
# async def process_code(message: Message, state: FSMContext) -> None:
#     await state.update_data(name=message.text)
#     await state.set_state(VerifyCode.verify_code)
#     # await message.answer(
#     #     f"Nice to meet you, {html.quote(message.text)}!\nDid you like to write bots?",
#     #     reply_markup=ReplyKeyboardMarkup(
#     #         keyboard=[
#     #             [
#     #                 KeyboardButton(text="Yes"),
#     #                 KeyboardButton(text="No"),
#     #             ]
#     #         ],
#     #         resize_keyboard=True,
#     #     ),
#     # )
#     print('okkkkk')

#
# # @router.message(
# #     ChatTypeFilter(chat_type=["private"]),
# #     # (StateFilter(None),
# #     FormattedCommandFilter(['/verify_code'])
# # )
# @router.callback_query(YDDCallback.filter(F.cb_type == "verify_code"),
#                        sta)
# async def process_verify_command(query: CallbackQuery, state: FSMContext):
#     await query.message.answer("Enter code:")
#     await state.set_state(VerifyCode.verify_code)
#
#     state_data = await state.get_data()
#
#     await query.message.answer(state_data['verify_code'])


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

