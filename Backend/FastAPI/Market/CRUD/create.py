from fastapi import HTTPException

import asyncio
import uuid

from authentication.models.models import Login, User
from authentication.password.password import hash_tool
from authentication.refresh.set_token import set_refresh_token
from config.database.database_connection import db_helper
from config.redis.redis_connection import rd_connection

from CRUD.models import User as TableUser
from market.models.models import ItemInfo
from CRUD.models import Items

async def register_user(user: User):
    async with db_helper.get_db_session() as session:

        login, password = await asyncio.create_task(
            hash_tool(
                Login(
                    login=user.login,
                    password=user.password
                )
            )
        )
        uuid_ = uuid.uuid4()
        new_record = TableUser(
            uuid=uuid_,
            name=user.name,
            login=login,
            password=password
        )
        session.add(new_record)
        try:
            await session.commit()
        except:
            return None, None, None
        access_token = await asyncio.create_task(set_refresh_token(str(uuid_), user.name))

        return str(uuid_), user.name, access_token

async def add_item(item: ItemInfo):

    async with db_helper.get_db_session() as session:

        new_record = Items(
            name=item.name,
            weight=item.weight,
            price=item.price
        )
        session.add(new_record)

        await session.commit()