from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from language import *

def keyboard_(obj):

    key_ = {"ru":Ru(), "az":Az(), "bel":Br(), "kz":Kz(), "kirg":Kirg(), "ozb":Uz(), "taj":Tg(),}

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text=key_[obj].register, url="https://mastergroosha.github.io/aiogram-3-guide/routers/")
            ],
            [
                InlineKeyboardButton(text=key_[obj].help, url="https://t.me/Jigaro01")
            ],
        ]
    )
    return keyboard