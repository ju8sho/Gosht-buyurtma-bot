import asyncio
import logging
import sys

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from handlers import routers_list
from bot_params import bot
from commands import set_bot_commands


dp = Dispatcher(storage=MemoryStorage())

async def main() -> None:
    await set_bot_commands()

    dp = Dispatcher()
    dp.include_routers(*routers_list)

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())