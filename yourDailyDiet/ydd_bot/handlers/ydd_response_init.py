from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery

from api.get_user import verify_user_code
from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter

from handlers.states import VerifyCode

from keyboards.meal_types_keyboard import YDDCallback
from keyboards.auth_keyboard import get_keyboard

from messages import WELCOME_MESSAGE

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
    await state.update_data(verify_code=message.text)

    resp = await verify_user_code(code=message.text,
                                  user_id=message.from_user.id)


    await message.answer(
        f"Nice to meet you, {message.text}!\nDid you like to "
        f"write bots?")
    await state.clear()
