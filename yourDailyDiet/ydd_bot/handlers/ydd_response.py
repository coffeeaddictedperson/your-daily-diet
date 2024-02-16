import asyncio

import aiohttp
from aiohttp import web

from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.filters import Command
from aiogram.types import Message

from filters.chat_type import ChatTypeFilter
from filters.command_type import CommandTypeFilter
from handlers.call_api import get_meal_types

from messages import WELCOME_MESSAGE, BTN_BREAKFAST
from keyboards.inline_keyboard import get_meal_types_keyboard

router = Router()

@router.message(
    ChatTypeFilter(chat_type=["private"]),
    Command(commands=["start"]),
)
async def process_start_command(message: Message):
    print('Private chat: received start command')
    # send request to api to get meal types
    meal_types = await get_meal_types()
    keyboard = get_meal_types_keyboard(meal_types)
    await message.answer(WELCOME_MESSAGE, reply_markup=keyboard)

# @router.message(
#     ChatTypeFilter(chat_type=["private"]),
#     Command(commands=["breakfast"]),
# )
# async def process_start_command(message: Message):
#     print('Private chat: received start command')
#     await message.answer(WELCOME_MESSAGE)



