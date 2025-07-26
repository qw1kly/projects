from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🇷🇺 Русский", callback_data="ru")
        ],
        [
            InlineKeyboardButton(text="🇦🇿 Azərbaycan dili", callback_data="az")
        ],
        [
            InlineKeyboardButton(text="🇧🇾 Беларуская мова", callback_data="bel")
        ],
        [
            InlineKeyboardButton(text="🇰🇿 Қазақ тілі", callback_data="kz")
        ],
        [
            InlineKeyboardButton(text="🇰🇬 Кыргыз тили", callback_data="kirg")
        ],
        [
            InlineKeyboardButton(text="🇺🇿 Oʻzbek tili", callback_data="ozb")
        ],
        [
            InlineKeyboardButton(text="🇹🇯 Тоҷикӣ", callback_data="taj")
        ],
    ]
)