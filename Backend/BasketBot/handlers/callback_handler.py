import asyncio

from aiogram import Router, F
from aiogram.types import CallbackQuery, InputMediaPhoto

from keyboard.basket_keyboard import return_kb, add_item
from user.manager import manager
from keyboard.keyboards import keyboard

import items.items as ct
import inspect

classes = [obj for name, obj in inspect.getmembers(ct) if inspect.isclass(obj)]

router = Router()

@router.callback_query(F.data.in_(["11", "22", "33"]))
async def category(call: CallbackQuery):
    users = manager.users
    for i in range(len(users)):
        if users[i].user_id == call.from_user.id:
            users[i].category = call.data[:-1]
    await call.message.edit_text("Выберите услуги", reply_markup=await asyncio.create_task(return_kb(call.data, call.from_user.id)))

@router.callback_query(F.data.in_(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27']))
async def price_list(call: CallbackQuery):
    users = manager.users
    for i in range(len(users)):
        if users[i].user_id == call.from_user.id:
            if int(call.data) not in users[i].accepted:
                users[i].accepted.append(int(call.data))
    await call.message.edit_text("Выберите услуги:", reply_markup=await asyncio.create_task(add_item(call.from_user.id, call.data)))


@router.callback_query(F.data == 'back')
async def back(call: CallbackQuery):
    await call.message.edit_text("Выберите категорию: ", reply_markup=keyboard)


@router.callback_query(F.data == 'count')
async def count(call: CallbackQuery):
    price = 0
    title_text = ''
    price_text = ''
    users = manager.users
    for i in range(len(users)):
        if users[i].user_id == call.from_user.id:
            for j in range(len(classes)):
                if classes[j]().index in users[i].accepted:
                    price += classes[j]().price
                    title_text += classes[j]().title + "\n"
                    price_text += str(classes[j]().price) + "+"
            price_text = price_text[:-1] + "=" + str(price)
            final_basket = title_text + "\n" + price_text
            users[i].accepted = []
            break

    await call.message.answer(final_basket)