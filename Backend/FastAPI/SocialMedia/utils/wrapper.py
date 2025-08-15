import jwt
from config.getter import secret_key
import time
from fastapi import HTTPException

def outline(func):

    def wrapper(*args, **kwargs):

        id, token = args[0], args[-1]
        try:
            real_id = jwt.decode(token, secret_key, algorithms=['HS256'])
        except:
            real_id = {'id': None, "exp": 0}
        if real_id['id'] == id and real_id['exp'] > time.time():
            return func(*args, **kwargs)

        return HTTPException(401)

    return wrapper