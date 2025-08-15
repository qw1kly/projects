import asyncio

from fastapi import APIRouter, Depends, Cookie

from models.models import User, Subs, Posts
from CRUD.read import auth, get_subs, get_subscr, get_posts, get_user_posts, get_profile_info
from utils.wrapper import outline

router = APIRouter()


@router.get("/auth")
async def authentication(id, session_token: str = Cookie(None)):
    return await asyncio.create_task(auth(User, id, session_token))


@router.get("/subs")
@outline
async def subs_to(id, session_token: str = Cookie(None)):
    return await asyncio.create_task(get_subs(Subs, own_id=id))


@router.get("/subscr")
@outline
async def subscr_to(id, session_token: str = Cookie(None)):
    return await asyncio.create_task(get_subscr(Subs, own_id=id))


@router.get("/allposts")
@outline
async def all_posts(id, session_token: str = Cookie(None)):
    return await asyncio.create_task(get_posts(Posts))


@router.get("/userpost")
@outline
async def user_posts(id, session_token: str = Cookie(None)):
    return await asyncio.create_task(get_user_posts(Posts, user_id=id))


@router.get("/profile")
@outline
async def user_posts(id, session_token: str = Cookie(None)):
    return await asyncio.create_task(get_profile_info(User, user_id=id))
