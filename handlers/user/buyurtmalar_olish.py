from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.text_decorations import html_decoration as hd

from bot_params import ADMIN_IDS, bot
from state.buyurtma import BuyurtmaState

buyurtma_olish_router = Router()

buyurtmangizni_yozing = (
    f"{hd.bold('Buyurtmangizni yozing:')}\n\n"
    f"{hd.italic('Misol uchun:\n1kg go\'sht kerak, suvagi va yog\'i ko\'proq bo\'lsin, Palonchi ko\'chasi, palonchi uy')}"
)

xato_xabar = (
    f"{hd.bold('Xatolik yuz berdi!')}\n"
    f"{'Iltimos, buyurtma matnini to\'g\'ri kiriting yoki'} "
    f"{hd.italic('Buyurtma')} tugmasini qayta bosing."
)


@buyurtma_olish_router.message(F.text == "Buyurtma")
async def buyurtma_olish_handler(message: Message, state: FSMContext):
    await message.answer(buyurtmangizni_yozing)
    await state.set_state(BuyurtmaState.matn_kiritish)  # Foydalanuvchini state ga o'tkazamiz


@buyurtma_olish_router.message(BuyurtmaState.matn_kiritish)
async def buyurtma_matni_qabul_qilish(message: Message, state: FSMContext):

    try:
        # Foydalanuvchining buyurtma matnini qabul qilamiz
        buyurtma_matni = message.text.strip()  # Matnni olib, bo'sh joylarni kesamiz
        if not buyurtma_matni:
            raise ValueError("Buyurtma matni bo'sh bo'lishi mumkin emas.")
        elif buyurtma_matni in ["Mahsulotlar", "sdfdfgery", "sdkfjfg", "xizmatlar", "sdfa"]:
            await message.answer(message.chat.id, "Buyurtma matnini kiriting")
        else:
            user_fullname = message.from_user.full_name or "Ism ko'rsatilmagan"
            user_username = message.from_user.username
            user_id = message.from_user.id

            # Agar username mavjud bo'lsa, to'liq ism bilan birga ko'rsatamiz
            if user_username:
                user_link = f"{user_fullname} (@{user_username})"
            else:
                # Agar username mavjud bo'lmasa, faqat to'liq ismni ko'rsatamiz
                user_link = f'<a href="tg://user?id={user_id}">{user_fullname}</a>'


            admin_message = (
                f"{hd.bold('Yangi buyurtma!')}\n\n"
                f"{'Foydalanuvchi:'} {user_link}\n"
                f"{'Buyurtma matni:'}\n{buyurtma_matni}"
            )

            # Adminlarga xabar yuboramiz
            for admin in ADMIN_IDS:
                try:
                    await bot.send_message(admin, admin_message)
                except Exception as e:
                    print(f"Adminga xabar yuborishda xatolik: {e}")

                buyurtmangiz_qabul_qilindi = ( 
                f"{hd.bold('Buyurtmangiz qabul qilindi.')}\n"
                f"{'Admin siz bilan bog\'lanadi!'}\n\n"
                f"{hd.bold('Sizning buyurtma matningiz:')}\n{hd.italic(buyurtma_matni)}"
                )

            # Foydalanuvchiga tasdiqlash xabarini yuboramiz
            await message.answer(buyurtmangiz_qabul_qilindi)
            await state.clear()  # State ni tozalaymiz

    except Exception as e:
        # Xato xabarini tayyorlaymiz
        await message.answer(xato_xabar)
        print(f"Xato: {e}")  # Xato haqida log yozamiz
