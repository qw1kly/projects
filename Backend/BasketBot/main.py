import asyncio
from aiogram import Bot, Dispatcher

from config.config import token

from handlers import main_handler, callback_handler

bot = Bot(token)
dp = Dispatcher()

async def main():

    dp.include_routers(main_handler.router, callback_handler.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())