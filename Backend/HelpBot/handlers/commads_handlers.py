from aiogram import Router, F
from aiogram.types import Message, InputMediaPhoto
from aiogram.types.input_file import FSInputFile

from models.connection import Connect
from models.models import User
from models.get_data import get_data

from language import *

from keyboards.language_keyboard import keyboard
from keyboards.last_keyboard import keyboard_

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    connection = Connect()
    connection.open()
    key_ = {"ru":Ru(), "az":Az(), "bel":Br(), "kz":Kz(), "kirg":Kirg(), "ozb":Uz(), "taj":Tg(),}

    auth = get_data(message.from_user.id, connection.session)
    if not(auth):
        await message.answer("🌍 Выбери язык бота / Choose bot language", reply_markup=keyboard)
        connection.close()
    else:
        photo = FSInputFile(path="src/0cb4820d-72ce-4407-b0e8-806eb313176c.jfif")
        caption = key_[auth].text
        await message.answer_photo(photo,caption, reply_markup=keyboard_(auth))
        connection.close()



@router.message(F.text == '/language')
async def language(message: Message):
    pass