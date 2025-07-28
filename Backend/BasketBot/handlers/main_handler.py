from aiogram import Router, F
from aiogram.types import Message, InputMediaPhoto
from aiogram.types.input_file import FSInputFile

from keyboard.keyboards import keyboard

from user.user import User
from user.manager import manager

router = Router()

@router.message(F.text == '/start')
async def start(message: Message):
    user = User(message.from_user.id)
    manager.append_user(user)
    await message.answer("Выберите категорию: ", reply_markup=keyboard)