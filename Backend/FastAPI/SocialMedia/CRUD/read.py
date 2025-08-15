import asyncio

from config.database.database_connection import db_helper

from models.models import User, Posts, Subs
from tokens.JWT_token import set_refresh_token, get_access_token
from sqlalchemy import select

from fastapi import HTTPException

async def auth(user: User, id, token):
    if not(token):
        return HTTPException(401)
    async with db_helper.get_db_session() as session:
        query = select(user)
        users = await session.execute(query)
        objects = list(users.scalars().all())
        for i in range(len(objects)):
            if objects[i].id == id:
                val_token = asyncio.create_task(get_access_token(token, objects[i].refresh_token))
                break
        return val_token


async def get_posts(posts: Posts):

    async with db_helper.get_db_session() as session:

        query = select(posts)
        posts = await session.execute(query)
        objects = list(posts.scalars().all())
        for i in range(len(objects)):
            objects[i] = [objects[i].user_id, objects[i].id, objects[i].likes, objects[i].content]

    return objects


async def get_subs(subs: Subs, own_id):

    async with db_helper.get_db_session() as session:

        query = select(subs)
        subss = await session.execute(query)
        objects = list(subss.scalars().all())
        subscriber = []

        for i in range(len(objects)):
            if objects[i].owner_id == own_id:
                subscriber.append(objects[i].child_id)

    return subscriber


async def get_subscr(subs: Subs, own_id):
    async with db_helper.get_db_session() as session:

        query = select(subs)
        subscr = await session.execute(query)
        objects = list(subscr.scalars().all())
        subscriber = []

        for i in range(len(objects)):
            if objects[i].child_id == own_id:
                subscriber.append(objects[i].owner_id)

    return subscriber


async def get_user_posts(posts: Posts, user_id):

    async with db_helper.get_db_session() as session:

        query = select(posts)
        post = await session.execute(query)
        objects = list(post.scalars().all())
        user_posts = []

        for i in range(len(objects)):
            if objects[i].user_id == user_id:
                user_posts.append([objects[i].user_id, objects[i].id, objects[i].likes, objects[i].content])

    return user_posts


async def get_profile_info(user: User, user_id):
    async with db_helper.get_db_session() as session:

        query = select(user)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        for i in range(len(objects)):
            if objects[i].id == user_id:
                return [objects[i].id, objects[i].name, objects[i].surname, objects[i].age, objects[i].likes, objects[i].subscribers, objects[i].subscriptions, objects[i].posts]
    return HTTPException(400)