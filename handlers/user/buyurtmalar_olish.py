from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.text_decorations import html_decoration as hd

from bot_params import ADMIN_IDS, bot
from state.buyurtma import BuyurtmaState

buyurtma_olish_router = Router()

# Buyurtma matnini oldindan saqlab qo'yamiz
buyurtmangizni_yozing = (
    f"{hd.bold('Buyurtmangizni yozing:')}\n\n"
    f"{hd.italic('Misol uchun:\n1kg go\'sht kerak, suvagi va yog\'i ko\'proq bo\'lsin, Palonchi ko\'chasi, palonchi uy')}"
)

xato_xabar = (
    f"{hd.bold('Xatolik yuz berdi!')}\n"
    f"{'Iltimos, buyurtma matnini to\'g\'ri kiriting yoki'} "
    f"{hd.italic('Buyurtma')} tugmasini qayta bosing."
)

# Global o'zgaruvchi sifatida xabar ID sini saqlash uchun joy yaratamiz
last_message_id = None

@buyurtma_olish_router.message(F.text == "Buyurtma")
async def buyurtma_olish_handler(message: Message, state: FSMContext):
    global last_message_id
    
    # Agar eski xabar mavjud bo'lsa, uni o'chirishga harakat qilamiz
    if last_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=last_message_id)
        except Exception as e:
            print(f"Eski xabarni o'chirishda xatolik: {e}")

    # Yangi xabarni yuborish va uning ID sini saqlash
    sent_message = await message.answer(buyurtmangizni_yozing)
    last_message_id = sent_message.message_id

    # Foydalanuvchini state ga o'tkazamiz
    await state.set_state(BuyurtmaState.matn_kiritish)


@buyurtma_olish_router.message(BuyurtmaState.matn_kiritish)
async def buyurtma_matni_qabul_qilish(message: Message, state: FSMContext):
    global last_message_id

    # Foydalanuvchining buyurtma matnini qabul qilamiz
    buyurtma_matni = message.text.strip()  # Matnni olib, bo'sh joylarni kesamiz
    if not buyurtma_matni:
        await message.answer(xato_xabar)
        return

    user_fullname = message.from_user.full_name or "Ism ko'rsatilmagan"
    user_username = message.from_user.username
    user_id = message.from_user.id

    # Foydalanuvchi havolasini yaratish
    if user_username:
        user_link = f"{user_fullname} (@{user_username})"
    else:
        user_link = f'<a href="tg://user?id={user_id}">{user_fullname}</a>'

    admin_message = (
        f"{hd.bold('Yangi buyurtma!')}\n\n"
        f"{'Foydalanuvchi:'} {user_link}\n"
        f"{'Buyurtma matni:'}\n{buyurtma_matni}"
    )

    # Adminlarga xabar yuborish
    for admin in ADMIN_IDS:
        try:
            await bot.send_message(admin, admin_message)
        except Exception as e:
            print(f"Adminga xabar yuborishda xatolik: {e}")

    # Buyurtmangiz qabul qilindi xabarini yuborish
    buyurtmangiz_qabul_qilindi = (
        f"{hd.bold('Buyurtmangiz qabul qilindi.')}\n"
        f"{'Admin siz bilan bog\'lanadi!'}\n\n"
        f"{hd.bold('Sizning buyurtma matningiz:')}\n{hd.italic(buyurtma_matni)}"
    )

    # Agar eski xabar mavjud bo'lsa, uni o'chirish
    if last_message_id:
        try:
            await bot.delete_message(chat_id=message.chat.id, message_id=last_message_id)
        except Exception as e:
            print(f"Eski xabarni o'chirishda xatolik: {e}")

    # Foydalanuvchiga yangi xabar yuborish va ID sini saqlash
    sent_message = await message.answer(buyurtmangiz_qabul_qilindi)
    last_message_id = sent_message.message_id

    # State ni tozalash
    await state.clear()
