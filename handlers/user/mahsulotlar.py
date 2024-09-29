import sqlite3

from aiogram import F, Router
from aiogram.types import Message

mahsulot_router = Router()

@mahsulot_router.message(F.text == "Mahsulotlar")
async def show_products_handler(message: Message):
    connection = sqlite3.connect('products.db')
    cursor = connection.cursor()

    cursor.execute('SELECT name, price FROM products')
    products = cursor.fetchall()

    if products:
        product_list = "\n".join([f"{name}: {price} so'm" for name, price in products])
        await message.answer(f"Mavjud mahsulotlar:\n{product_list}")
    else:
        await message.answer("Mahsulotlar ro'yxati bo'sh.")

    connection.close()