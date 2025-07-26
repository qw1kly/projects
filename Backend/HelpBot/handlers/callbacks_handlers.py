from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto
from aiogram.types.input_file import FSInputFile

from language import *
from models.insert_data import add_user
from models.connection import Connect
from models.models import User

from keyboards.last_keyboard import keyboard_

router = Router()

@router.callback_query(F.data.in_(["ru", "az", "bel", "kz", "kirg", "ozb", "taj"]))
async def language(call: CallbackQuery):
    connection = Connect()
    connection.open()
    key_ = {"ru":Ru(), "az":Az(), "bel":Br(), "kz":Kz(), "kirg":Kirg(), "ozb":Uz(), "taj":Tg(),}
    add_user(User(user_id=str(call.from_user.id), language=call.data), connection.session)
    connection.close()
    photo = FSInputFile(path="src/0cb4820d-72ce-4407-b0e8-806eb313176c.jfif")
    caption = key_[call.data].text

    await call.message.answer_photo(photo, caption, reply_markup=keyboard_(key_[call.data]))