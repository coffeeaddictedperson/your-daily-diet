import asyncio
import os

from aiogram import Bot, Dispatcher
from handlers import ydd_response


async def main():
    token = os.getenv("API_TOKEN")
    bot = Bot(token=token)
    dp = Dispatcher()

    dp.include_router(ydd_response.router)

    print('Starting YDD bot...')

    # delete all old requests
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())