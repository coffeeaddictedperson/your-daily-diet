from aiogram.filters.callback_data import CallbackData


class YDDCallback(CallbackData, prefix="ydd_cb"):
    cb_type: str
    value: str
