from aiogram import Router
from aiogram.types import Message

from messages import UNKNOWN_COMMAND_MESSAGE

router = Router()


# None of the above commands are matched: show warning message
@router.message()
async def process_echo(message: Message):
    print('Private chat: received unregistered command')
    await message.answer(UNKNOWN_COMMAND_MESSAGE)
