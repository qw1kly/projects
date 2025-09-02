from fastapi import APIRouter, Depends

from authentication.utils.cookie_reader import get_token_from_cookie

router = APIRouter()


@router.get('/authentication')
async def authentication(cookies: dict = Depends(get_token_from_cookie)):

    return cookies


