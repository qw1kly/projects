import asyncio

from CRUD.utils.utils import creds_equal
from authentication.password.password import hash_tool
from config.database.database_connection import db_helper

from authentication.models.models import Login
from CRUD.models import User

from sqlalchemy import select

async def login_getter(creds: Login):
    login, password = await asyncio.create_task(hash_tool(creds))

    async with db_helper.get_db_session() as session:

        query = select(User)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        return await asyncio.create_task(creds_equal(login, password, objects))


