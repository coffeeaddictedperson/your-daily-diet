
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from keyboards.callback_data import YDDCallback
from messages import BTN_BREAKFAST, BTN_SNACK, BTN_DINNER

BTNS_PER_ROW = 4


def get_meal_types_keyboard(meal_types=None):
    if meal_types is None:
        meal_types = [BTN_BREAKFAST, BTN_SNACK, BTN_DINNER]

    buttons = []
    for cell, meal_type in enumerate(meal_types):
        callback_data = YDDCallback(
            cb_type="meal_type",
            value=meal_type.lower()
        ).pack()
        btn = InlineKeyboardButton(
            text=meal_type,
            callback_data=callback_data
        )
        if cell % BTNS_PER_ROW == 0:
            buttons.append([])
        buttons[-1].append(btn)

    return InlineKeyboardMarkup(
        inline_keyboard=buttons,
    )
