from aiogram.fsm.state import State, StatesGroup


class DeleteProductState(StatesGroup):
    mahsulotni_kutish = State()

class MahsulotQoshishState(StatesGroup):
    mahsulot_nomi = State()
    mahsulot_narxi = State()

class BuyurtmaState(StatesGroup):
    matn_kiritish = State()