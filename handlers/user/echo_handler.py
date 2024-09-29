from aiogram import F, Router
from aiogram.filters import StateFilter
from aiogram.types import Message

echo_router = Router()

@echo_router.message(F.text, StateFilter(None))
async def bot_echo(message: Message):
    text = ["Echo no state.", "Xabar:", message.text]

    await message.answer("\n".join(text))
