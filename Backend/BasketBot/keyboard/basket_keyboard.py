from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import items.items as ct
import inspect

from user.manager import manager

classes = [obj for name, obj in inspect.getmembers(ct) if inspect.isclass(obj)]



async def return_kb(iddx, id):

    iddx = iddx[:-1]
    kb = {1: [], 2: [], 3: []}

    users = manager.users
    users_accepted = []
    users_category = None
    for i in range(len(users)):
        if users[i].user_id == id:
            users_accepted = users[i].accepted
            users_category = users[i].category
            break
    for i in classes:
        object_ = i()
        if str(object_.category) == str(users_category) and (object_.index) in users_accepted:
            kb[object_.category].append([InlineKeyboardButton(text=object_.title+"✅", callback_data=str(object_.index))])
        else:
            kb[object_.category].append([InlineKeyboardButton(text=object_.title, callback_data=str(object_.index))])
    kb[int(iddx)].append([InlineKeyboardButton(text="Готово", callback_data="count")])
    kb[int(iddx)].append([InlineKeyboardButton(text="Назад", callback_data="back")])
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=
            kb[int(iddx)]
    )

    return keyboard

async def add_item(id, index):
    kb = {1: [], 2: [], 3: []}
    users = manager.users
    users_accepted = []
    users_category = None

    for i in range(len(users)):
        if users[i].user_id == id:
            users_accepted = users[i].accepted
            users_category = users[i].category
            break

    for i in classes:
        object_ = i()
        if str(object_.category) == str(users_category) and (object_.index) in users_accepted:
            kb[object_.category].append([InlineKeyboardButton(text=object_.title+"✅", callback_data=str(object_.index))])
        else:
            kb[object_.category].append([InlineKeyboardButton(text=object_.title, callback_data=str(object_.index))])
    kb[int(users_category)].append([InlineKeyboardButton(text="Готово", callback_data="count")])
    kb[int(users_category)].append([InlineKeyboardButton(text="Назад", callback_data="back")])

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=
        kb[int(users_category)]
    )

    return keyboard

