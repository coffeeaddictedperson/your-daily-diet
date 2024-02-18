from aiogram import Router, F
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery

from filters.chat_type import ChatTypeFilter
from filters.command_type import FormattedCommandFilter

from api.get_ydd import get_meal_types, get_random_meal
from handlers.check_user import get_verification_message

from messages import WELCOME_MESSAGE, GET_YOUR_MEAL
from keyboards.auth_keyboard import get_keyboard
from keyboards.meal_types_keyboard import get_meal_types_keyboard, YDDCallback

router = Router()


# Get your meal command, private channel only
@router.message(
    ChatTypeFilter(chat_type=["private"]),
    FormattedCommandFilter([GET_YOUR_MEAL, '/try_again']),
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
        result = await get_random_meal(
            meal_type=callback_data.value,
            user_id=query.message.chat.id
        )
        message_text = get_verification_message(result.get('user_status'))

        if message_text is not None:
            print('Private chat: verification not passed (/meal_type)')
            await query.message.answer(message_text,
                                       reply_markup=get_keyboard(query.message))
            return

        meal = result.get('meal')
        description = result.get('description')
        is_vegetarian = result.get('is_vegetarian')

        if meal != 'None' and meal is not None:
            await query.message.edit_text(
                f'Looking for {callback_data.value} for you...')

            answer = f'🍽🍽🍽 YDD suggests for {callback_data.value} 🍽🍽🍽'
            answer += f'\n\n{meal}'
            if is_vegetarian:
                answer += ' (🌱)'
            answer += f'\n\n<i>{description}</i>'
            await query.message.edit_text(answer, parse_mode=ParseMode.HTML)
        else:
            await query.message.answer(
                f'No meal found for {callback_data.value}')
    except:
        print('Private chat: meal type: error occurred')
        await query.message.answer(f'No meal found for {callback_data.value}. '
                                   f'Try again later.')
