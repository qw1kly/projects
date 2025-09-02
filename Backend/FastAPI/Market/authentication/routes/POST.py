from fastapi import APIRouter, Depends

from CRUD.create import register_user
from CRUD.read import login_getter
from authentication.models.models import Login, User


router = APIRouter()


@router.post('/login')
async def login(credentials: Login = Depends(login_getter)):
    return {"message": "login", "uuid": credentials[0], "name": credentials[1], "token": credentials[2]}


@router.post('/register')
async def register(credentials: User = Depends(register_user)):

    return {"message": "register", "uuid": credentials[0], "name": credentials[1], "token": credentials[2]}