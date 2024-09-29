from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router, F

from filters.admin_filter import AdminFilter
from keyboard.keyboards import admin_keyboard
from bot_params import bot, Bot

from bot_params import ADMIN_IDS

admin_router = Router()

@admin_router.message(CommandStart(), AdminFilter())
async def admin_start_handler(message: Message) -> None:
    await message.answer("Salom admin!", reply_markup=admin_keyboard)
