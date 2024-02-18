import asyncio
import os

from aiogram import Bot, Dispatcher

from handlers import ydd_response_init, ydd_response_meals, ydd_response_other


async def main():
    token = os.getenv("API_TOKEN")
    bot = Bot(token=token)
    dp = Dispatcher()
    print('Starting YDD bot...')

    # delete all old requests
    print('Deleting old messages...')
    await bot.delete_webhook(drop_pending_updates=True)

    # init listeners
    print('Init listeners...')
    dp.include_router(ydd_response_init.router)
    dp.include_router(ydd_response_meals.router)
    dp.include_router(ydd_response_other.router)

    # start polling
    print('Starting polling...')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
