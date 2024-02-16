from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from messages import BTN_BREAKFAST, BTN_SNACK, BTN_DINNER

BTNS_PER_ROW = 4

def get_meal_types_keyboard(meal_types=None):
    if meal_types is None:
        meal_types = [BTN_BREAKFAST, BTN_SNACK, BTN_DINNER]

    buttons = []
    for cell, meal_type in enumerate(meal_types):
        btn = KeyboardButton(text=meal_type)
        if cell % BTNS_PER_ROW == 0:
            buttons.append([])
        buttons[-1].append(btn)

    return ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=False
    )
