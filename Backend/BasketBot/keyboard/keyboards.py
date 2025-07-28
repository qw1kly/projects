from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Рентген", callback_data="11")
        ],
        [
            InlineKeyboardButton(text="Терапия", callback_data="22")
        ],
        [
            InlineKeyboardButton(text="Хирургия", callback_data="33")
        ],
    ]
)