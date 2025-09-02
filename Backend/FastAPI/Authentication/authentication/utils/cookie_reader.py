import asyncio

from fastapi import Cookie, HTTPException

from authentication.refresh.get_token import get_refresh_token
from authentication.utils.decorators import outline
import time

@outline
async def get_token_from_cookie(token: str | None = Cookie(default=None, alias="auth_token"), uuid: str | None = Cookie(default=None, alias="uuid"), name: str | None = Cookie(default=None, alias="name"), decoder = None):
    if not(token):
        return {"message": "401", "type": 'Token required!'}

    if uuid == decoder.uuid and name == decoder.name and decoder.exp > time.time():
        return {"message": "200", "type": "auth_done"}
    elif uuid == decoder.uuid and name == decoder.name and decoder.exp <= time.time():
        accss_token = await asyncio.create_task(get_refresh_token(uuid, name))
        if accss_token == '401':
            return {"message": "401", "type": "Token expired!"}
        return {"message": "200", "type": "auth", "token": accss_token}

    return {"message": "401", "type": "Something went wrong!"}
