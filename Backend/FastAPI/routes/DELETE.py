import asyncio

from fastapi import APIRouter, Depends, Cookie

from models.models import User, Subs, Posts
from CRUD.delete import *
from utils.wrapper import outline


router = APIRouter()


@router.delete('/deleteposts')
@outline
async def delete_posts(id, post_id, session_token: str = Cookie(None)):
    return await asyncio.create_task(delete_post(post_id=post_id))


@router.delete('/deletesubs')
@outline
async def delete_sub(id, owner_id, child_id, session_token: str = Cookie(None)):
    return await asyncio.create_task(delete_subs(owner_id=owner_id, child_id=child_id))
