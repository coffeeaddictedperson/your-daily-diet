from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from api.get_user import verify_user_code
from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter
from handlers.check_user import verify_user_and_answer, GET_MEAL_TYPES_STEP

from handlers.states import VerifyCode
from keyboards.get_meal_keyboard import get_meal_keyboard

from keyboards.meal_types_keyboard import YDDCallback
from keyboards.auth_keyboard import get_keyboard

from messages import WELCOME_MESSAGE

USER_VERIFIED = "user_verified"
USER_EXPIRED = "user_expired"
USER_NON_VERIFIED = "user_non_verified"
USER_NOT_FOUND = "user_not_found"

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
@router.callback_query(YDDCallback.filter(F.cb_type == "verify_code"))
async def process_verify_command(query: CallbackQuery, state: FSMContext):
    print('Private chat: received /verify_code command')
    await state.set_state(VerifyCode.enter_in_verification_mode)
    await query.message.answer('Enter code:')


@router.message(VerifyCode.enter_in_verification_mode)
async def process_code(message: Message, state: FSMContext) -> None:
    print('Private chat: received verification')
    code = message.text
    await state.clear()

    user_status = await verify_user_code(code=code,
                                  user_id=message.from_user.id)

    message_text, kb = verify_user_and_answer(user_status, message)
    if message_text and kb:
        print('Private chat: verification not passed')
        await message.answer(message_text, reply_markup=kb)
    else:
        print('Private chat: verification successful')
        await message.answer(WELCOME_MESSAGE, reply_markup=get_meal_keyboard())

