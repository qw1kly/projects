import asyncio

from fastapi import APIRouter, Depends, Cookie

from models.models import User, Subs, Posts
from CRUD.create import *
from CRUD.update import *
from utils.wrapper import outline


router = APIRouter()


@router.post("/register")
async def register_user(user_info):
    return await asyncio.create_task(register(user_info=user_info))


@router.post("/add/post")
@outline
async def add_post(id, text, session_token: str = Cookie(None)):
    return await asyncio.create_task(create_post(id=id, content=text))


@router.post("/add/sub")
@outline
async def add_subs(id, own, chl, session_token: str = Cookie(None)):
    return await asyncio.create_task(add_sub(owner=own, child=chl))


@router.post("/like")
@outline
async def like(id, user_id, post_id, session_token: str = Cookie(None)):
    return await asyncio.create_task(update_posts_likes(posts=Posts, user_id=user_id, id=post_id))


@router.post("/refreshtoken")
@outline
async def refr_token(id, password):
    return await asyncio.create_task(update_refresh_token(user=User, id=id, password=password))

