from fastapi import APIRouter, Depends, Cookie

from CRUD.create import add_item
from CRUD.read import admin_identificator
from authentication.utils.cookie_reader import get_token_from_cookie
from market.models.models import ItemInfo

router = APIRouter()

@router.post('/add_item')
async def market(authentication_message: dict = Depends(get_token_from_cookie), item: ItemInfo = Depends(add_item)):
    if authentication_message['message'] == '200':
        return {"message": "200", "type": "Item added"}
    return authentication_message