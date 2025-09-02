from fastapi import Cookie
import asyncio

from CRUD.utils.utils import creds_equal
from authentication.password.password import hash_tool
from config.database.database_connection import db_helper

from authentication.models.models import Login
from CRUD.models import User, Items, Admin

from sqlalchemy import select

async def login_getter(creds: Login):
    login, password = await asyncio.create_task(hash_tool(creds))

    async with db_helper.get_db_session() as session:

        query = select(User)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        return await asyncio.create_task(creds_equal(login, password, objects))


async def get_items():

    async with db_helper.get_db_session() as session:

        query = select(Items)
        items = await session.execute(query)
        objects = list(items.scalars().all())

        return objects

async def get_item(item_id: int):

    async with db_helper.get_db_session() as session:

        query = select(Items)
        items = await session.execute(query)
        objects = list(items.scalars().all())

        for i in range(len(objects)):
            if objects[i][0] == item_id:
                return list(objects[i])
        return [{"message": "404", "type": "Not found"}]

async def admin_identificator(uuid: str | None = Cookie(default=None, alias="uuid")):

    async with db_helper.get_db_session() as session:

        query = select(Admin)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        for i in range(len(objects)):

            if objects[i][0] == uuid:
                return True
        return False