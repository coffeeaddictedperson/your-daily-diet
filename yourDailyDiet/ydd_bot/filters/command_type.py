from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

class CommandTypeFilter(BaseFilter):
    def __init__(self, text: Union[str, list]):
        self.text = text

    async def __call__(self, message: Message) -> bool:
        return message.text == self.text
