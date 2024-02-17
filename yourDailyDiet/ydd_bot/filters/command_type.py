from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

class FormattedCommandFilter(BaseFilter):
    def __init__(self, commands: list[str] | str):
        if isinstance(commands, str):
            commands = [commands]

        self.commands = list(map(FormattedCommandFilter.format_command, commands))

    @staticmethod
    def format_command(command: str) -> str:
        return (command.strip().lower()
                .replace('/', '')
                .replace('-', '')
                .replace(' ', ''))

    async def __call__(self, message: Message) -> bool:
        return FormattedCommandFilter.format_command(
            message.text) in self.commands
