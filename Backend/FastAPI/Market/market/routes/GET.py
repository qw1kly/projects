from fastapi import APIRouter, Depends
from fastapi_paginate import paginate
from CRUD.read import get_items, get_item
from authentication.utils.cookie_reader import get_token_from_cookie
from typing import Annotated

router = APIRouter()

@router.get('/items')
async def market(authentication_message: dict = Depends(get_token_from_cookie), items: list = Depends(get_items)):
    if authentication_message['message'] == '200':
        return paginate(items)
    return authentication_message


@router.get('/items/{item_id}')
async def one_item(
    item_id: int,
    item: Annotated[list, Depends(get_item)],
    authentication_message: dict = Depends(get_token_from_cookie),
):
    if authentication_message['message'] == '200':
        return item
    return authentication_message
