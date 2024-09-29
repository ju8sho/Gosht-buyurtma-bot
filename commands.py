from aiogram.types import BotCommand, BotCommandScopeDefault
from bot_params import bot


async def set_bot_commands():
    commands = [
        BotCommand(command="start", description="Botni ishga tushirish"),
        BotCommand(command="help", description="Yordam olish"),
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())