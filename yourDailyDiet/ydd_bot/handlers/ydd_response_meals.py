from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter

from handlers.call_api import get_meal_types, get_random_meal

from messages import WELCOME_MESSAGE, GET_YOUR_MEAL
from keyboards.meal_types_keyboard import get_meal_types_keyboard, YDDCallback

router = Router()


# Get your meal command, private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    FormattedCommandFilter([GET_YOUR_MEAL]),
)
async def process_echo(message: Message):
    print('Private chat: received get_your_meal command')
    # send request to api to get meal types
    meal_types = await get_meal_types()
    keyboard = get_meal_types_keyboard(meal_types)
    await message.answer(WELCOME_MESSAGE, reply_markup=keyboard)


@router.callback_query(YDDCallback.filter(F.cb_type == "meal_type"))
async def process_ydd_command(query: CallbackQuery, callback_data: YDDCallback):
    print('Private chat: received /meal_type command')
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
