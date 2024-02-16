from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from filters.chat_type import ChatTypeFilter
from filters.command_type import CommandTypeFilter

from handlers.call_api import get_meal_types, get_random_meal

from messages import WELCOME_MESSAGE, UNKNOWN_COMMAND_MESSAGE
from keyboards.inline_keyboard import get_meal_types_keyboard, YDDCallback
from keyboards.keyboard import get_keyboard, GET_YOUR_MEAL

router = Router()

# start command , private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    Command(commands=["start"]),
)
async def process_start_command(message: Message):
    print('Private chat: received start command')
    await message.answer(WELCOME_MESSAGE, reply_markup=get_keyboard())

# Get your meal command, private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    CommandTypeFilter(text=GET_YOUR_MEAL),
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
        meal = await get_random_meal()
        await query.message.answer(f'Your meal is {meal}')
    except:
        await query.message.answer(f'No meal found for {callback_data.value}')


@router.message()
async def process_echo(message: Message):
    await message.answer(UNKNOWN_COMMAND_MESSAGE)
