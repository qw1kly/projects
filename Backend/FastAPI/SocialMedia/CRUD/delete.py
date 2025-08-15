import asyncio

from config.database.database_connection import db_helper

from models.models import User, Posts, Subs
from tokens.JWT_token import set_refresh_token
from sqlalchemy import delete


async def delete_post(post_id):

    async with db_helper.get_db_session() as session:

        del_ = (delete(Posts)
                .where(Posts.id == post_id))

        await session.execute(del_)

        await session.commit()


async def delete_subs(owner_id, child_id):
    async with db_helper.get_db_session() as session:
        del_ = (delete(Subs)
                .where(Subs.owner_id == owner_id and Subs.child_id == child_id))

        await session.execute(del_)

        await session.commit()