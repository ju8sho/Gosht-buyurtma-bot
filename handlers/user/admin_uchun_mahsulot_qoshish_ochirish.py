from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


from db import add_product, delete_product, get_all_products
from filters.admin_filter import AdminFilter
from state.buyurtma import MahsulotQoshishState, DeleteProductState

mahsulot_qoshish_ochirish_korish_router = Router()

nomini_kiritish = "Mahsulot nomini kiriting!"
narxni_kiritish = "Mahsulot narxini kiriting!"

@mahsulot_qoshish_ochirish_korish_router.message(F.text == "Mahsulot qo'shish", AdminFilter())
async def mahsulot_qoshish(message: Message, state: FSMContext):
    # nomini_kiritish = "Mahsulot nomini kiriting!"
    await message.answer(nomini_kiritish)
    await state.set_state(MahsulotQoshishState.mahsulot_nomi)


@mahsulot_qoshish_ochirish_korish_router.message(MahsulotQoshishState.mahsulot_nomi)
async def mahsulot_qoshish(message: Message, state: FSMContext):
    mahsulot_nomi = message.text
    # narxni_kiritish = "Mahsulot narxini kiriting!"
    await state.update_data(name=mahsulot_nomi)
    await message.answer(narxni_kiritish)
    await state.set_state(MahsulotQoshishState.mahsulot_narxi)


@mahsulot_qoshish_ochirish_korish_router.message(MahsulotQoshishState.mahsulot_narxi)
async def get_product_price(message: Message, state: FSMContext):
    data = await state.get_data()
    name = data['name']
    try:
        price = float(message.text)
        add_product(name, price)
        await message.answer(f"Mahsulot '{name}' {price} narxda qo'shildi!")
    except ValueError:
        await message.answer("Noto'g'ri narx kiritildi. Iltimos, raqam kiriting.")
    await state.clear()



# Mahsulotlarni ko'rsatish va o'chirish uchun ID ni kiritish
@mahsulot_qoshish_ochirish_korish_router.message(F.text == "Mahsulot o'chirish", AdminFilter())
async def start_delete_product(message: Message, state: FSMContext):
    products = get_all_products()
    if not products:
        await message.answer("Mahsulotlar mavjud emas.")
        return

    product_list = "\n".join([f"{p[0]}. {p[1]} - {p[2]} so'm" for p in products])
    await message.answer(f"Mavjud mahsulotlar:\n{product_list}\n\nO'chirmoqchi bo'lgan mahsulot ID raqamini kiriting:")
    await state.set_state(DeleteProductState.mahsulotni_kutish)

@mahsulot_qoshish_ochirish_korish_router.message(DeleteProductState.mahsulotni_kutish)
async def delete_product_by_id(message: Message, state: FSMContext):
    try:
        product_id = int(message.text)
        delete_product(product_id)
        await message.answer(f"Mahsulot ID {product_id} o'chirildi.")
    except ValueError:
        await message.answer("Noto'g'ri ID kiritildi. Iltimos, raqam kiriting.")
    
    await state.clear()


@mahsulot_qoshish_ochirish_korish_router.message(F.text == "Mahsulotlar", AdminFilter())
async def show_products_handler(message: Message):
    # Mahsulotlar ro'yxatini olish
    products = get_all_products()

    if products:
        # Har bir mahsulot uchun nomi va narxini chiqaramiz
        product_list = "\n".join([f"{p[1]}: {p[2]} so'm" for p in products])  # p[1] - name, p[2] - price
        await message.answer(f"Mavjud mahsulotlar:\n{product_list}")
    else:
        await message.answer("Mahsulotlar ro'yxati bo'sh.")

