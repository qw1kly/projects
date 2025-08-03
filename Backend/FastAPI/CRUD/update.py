import asyncio

from config.database.database_connection import db_helper

from models.models import User, Posts
from tokens.JWT_token import set_refresh_token, get_access_token
from sqlalchemy import update, select
from tokens.password import hash_password

from fastapi import HTTPException

from tokens.password import hash_password


async def update_refresh_token(user: User, id, password):
    async with db_helper.get_db_session() as session:
        query = select(user)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        for i in range(len(objects)):
            if objects[i].id == id:
                current_password = objects[i].password
                break

        hashed_password = await asyncio.create_task(hash_password(password))

        if current_password == hashed_password:
            new_tokens = await asyncio.create_task(set_refresh_token(id))

            ref_token = (
                update(user)
                .where(user.id == id)
                .values(refresh_token=new_tokens[0])
            )

            await session.execute(ref_token)
            await session.commit()

            return new_tokens[1]
        return HTTPException(401)


async def update_subscr(user: User, owner_id, child_id):

    if owner_id == child_id:
        return HTTPException(400)

    async with db_helper.get_db_session() as session:
        query = select(user)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        for i in range(len(objects)):
            if objects[i].id == owner_id:
                current_subscr = objects[i].subscriptions
                break

        for i in range(len(objects)):
            if objects[i].id == child_id:
                current_subs = objects[i].subscribers
                break

        new_subscr = (
            update(user)
            .where(user.id == id)
            .values(subscriptions=current_subscr + 1)
        )

        new_subs = (
            update(user)
            .where(user.id == id)
            .values(subscribers=current_subs + 1)
        )

        await session.execute(new_subscr)
        await session.execute(new_subs)
        await session.commit()

async def update_posts(user: User, id):
    async with db_helper.get_db_session() as session:
        query = select(user)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        for i in range(len(objects)):
            if objects[i].id == id:
                current_posts = objects[i].posts
                break

        new_subs = (
            update(user)
            .where(user.id == id)
            .values(posts=current_posts+1)
        )

        await session.execute(new_subs)
        await session.commit()

async def update_likes(user: User, id):
    async with db_helper.get_db_session() as session:
        query = select(user)
        users = await session.execute(query)
        objects = list(users.scalars().all())

        for i in range(len(objects)):
            if objects[i].id == id:
                current_likes = objects[i].likes
                break

        new_subs = (
            update(user)
            .where(user.id == id)
            .values(likes=current_likes+1)
        )

        await session.execute(new_subs)
        await session.commit()


async def update_posts_likes(posts: Posts, user_id, id):
    async with db_helper.get_db_session() as session:
        query = select(posts)
        posts = await session.execute(query)
        objects = list(posts.scalars().all())

        for i in range(len(objects)):
            if objects[i].user_id == user_id and objects[i].id == id:
                current_likes = objects[i].likes
                break

        new_subs = (
            update(Posts)
            .where(Posts.id == id)
            .values(likes=current_likes + 1)
        )

        await session.execute(new_subs)
        await session.commit()

        await asyncio.gather(update_posts(User, user_id), update_likes(User, user_id))

