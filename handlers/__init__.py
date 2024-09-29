from handlers.user.admin_handler import admin_router
from handlers.user.start_help_handler import star_help_routers
from handlers.user.buyurtmalar_olish import buyurtma_olish_router
from handlers.user.admin_uchun_mahsulot_qoshish_ochirish import mahsulot_qoshish_ochirish_korish_router
from handlers.user.mahsulotlar import mahsulot_router
from handlers.user.echo_handler import echo_router



routers_list = [
    admin_router,
    star_help_routers,
    buyurtma_olish_router,
    mahsulot_qoshish_ochirish_korish_router,
    mahsulot_router,
    echo_router,  # Add more handlers here if needed!
]

__all__ = [
    "routers_list",
]