from aiogram.fsm.state import StatesGroup, State


class VerifyCode(StatesGroup):
    enter_in_verification_mode = State()
    verify_code = State()
