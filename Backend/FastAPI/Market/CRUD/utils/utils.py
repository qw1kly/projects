import asyncio

from authentication.refresh.get_token import get_refresh_token
from authentication.refresh.set_token import set_refresh_token
from config.redis.redis_connection import rd_connection
from fastapi import HTTPException

async def creds_equal(login, password, objects):

    for i in range(len(objects)):
        if login == objects[i].login and password == objects[i].password:

            refresh_token = rd_connection.get(objects[i].uuid)

            if not(refresh_token):

                jwt_token = await asyncio.create_task(set_refresh_token(objects[i].uuid, objects[i].name))

            elif refresh_token:

                jwt_token = await asyncio.create_task(get_refresh_token(objects[i].uuid, objects[i].name))

            return objects[i].uuid, objects[i].name, jwt_token

    return None, None, None