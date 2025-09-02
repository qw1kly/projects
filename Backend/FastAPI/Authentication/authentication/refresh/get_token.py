import asyncio

from fastapi import HTTPException

from authentication.access.set_token import set_access_token
from config.redis.redis_connection import rd_connection

async def get_refresh_token(uuid, name):

    token = rd_connection.get(uuid)

    if not(token):

        return "401"

    access_token = await asyncio.create_task(set_access_token(uuid, name))

    return access_token