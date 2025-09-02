from fastapi import HTTPException
import jwt
from functools import wraps
from dotenv import load_dotenv
import os
from hashlib import sha256

from authentication.models.models import TokenInfo, Login

load_dotenv()

secret_key = os.getenv("secret_key")

def outline(func):

    @wraps(func)
    async def wrapper(*args, decoder=None, **kwargs):
        try:
            valid_token = jwt.decode(kwargs['token'], secret_key, algorithms=['HS256'], options={"verify_exp": False})
            valid_token = TokenInfo(uuid=valid_token['uuid'], name=valid_token['name'], exp=valid_token['exp'])
        except:
            return {"message": "401", "type": "Token required!"}

        return await func(*args, decoder=valid_token, **kwargs)

    return wrapper




