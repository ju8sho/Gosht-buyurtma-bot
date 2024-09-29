from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# Bu foydalanuvchilar uchun kinopkalar
main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Buyurtma"), KeyboardButton(text="Mahsulotlar")]
    ],
    resize_keyboard=True
)
# bu admin uchun kinopkalar
admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Mahsulot qo'shish")],
        [KeyboardButton(text="Mahsulot o'chirish")],
        [KeyboardButton(text="Mahsulotlar")],
    ],
    resize_keyboard=True
)
######################
