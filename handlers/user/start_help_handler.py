from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram import html, Router, F
from aiogram.utils.text_decorations import html_decoration as hd

from bot_params import ADMIN_IDS
from keyboard.keyboards import main_keyboard
from aiogram.fsm.context import FSMContext


star_help_routers = Router()

@star_help_routers.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=main_keyboard)



@star_help_routers.message(Command("help"))
async def help_handler(message: Message) -> None:
    help_text = (
        f"{hd.bold('Salom!')} Sizga yordam berish uchun shu yerda turibman.\n\n"
        f"{hd.bold('Mavjud buyruqlar:')}\n"
        f"{hd.bold('/start')} - Botni ishga tushirish\n"
        f"{hd.bold('Buyurtma')} - Buyurtma berish uchun tugma.\n"
        f"{hd.bold('Mahsulotlar')} - Mavjud mahsulotlar ro'yxatini ko'rsatish.\n\n"
        "Agar siz 'Buyurtma' tugmasini bossangiz, siz o'z buyurtmangizni berishingiz mumkin.\n"
        "Agar 'Mahsulotlar' tugmasini bossangiz, siz mavjud mahsulotlar ro'yxatini ko'rishingiz mumkin."
    )

    await message.answer(help_text)

