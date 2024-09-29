from aiogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
# Admin IDlari
ADMIN_IDS = []
admin_ids_str = getenv("ADMIN_IDS", "")
if admin_ids_str:
    ADMIN_IDS = list(map(int, admin_ids_str.split(",")))

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))