import asyncio
from aiogram import Bot, Dispatcher

from handlers import commads_handlers, callbacks_handlers
from config import token

bot = Bot(token)
dp = Dispatcher()

async def main():

    dp.include_routers(commads_handlers.router, callbacks_handlers.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())