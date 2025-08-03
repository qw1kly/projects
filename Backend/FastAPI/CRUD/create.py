import asyncio

from CRUD.update import update_posts, update_subscr
from config.database.database_connection import db_helper

from models.models import User, Posts, Subs
from tokens.JWT_token import set_refresh_token
from sqlalchemy import select

from tokens.password import hash_password


async def register(user_info):
    password, name, surname, age = user_info

    async with db_helper.get_db_session() as session:
        token_gen = await asyncio.create_task(set_refresh_token(User.id))

        new_record = User(
            password=await asyncio.create_task(hash_password(password)),
            name=name,
            surname=surname,
            age=age,
            subscribers=0,
            subscriptions=0,
            posts=0,
            likes=0,
            refresh_token=token_gen[0]
        )
        session.add(new_record)

        await session.commit()

        return token_gen[1]


async def create_post(id, content):
    async with db_helper.get_db_session() as session:

        new_record = Posts(
            user_id=id,
            likes=0,
            content=content
        )
        session.add(new_record)

        await session.commit()
        await asyncio.create_task(update_posts(User, id=id))

        return {"response": 'ok'}


async def add_sub(owner, child):
    async with db_helper.get_db_session() as session:

        new_record = Subs(
            owner_id=owner,
            child_id=child
        )
        session.add(new_record)

        await session.commit()
        await asyncio.create_task(update_subscr(User, owner_id=owner, child_id=child))

        return {"response": 'ok'}
