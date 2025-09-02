from hashlib import sha256

from authentication.models.models import Login


async def hash_tool(crdn: Login):

    hashed_login = sha256(crdn.login.encode('utf-8')).hexdigest()
    hashed_password = sha256(crdn.password.encode('utf-8')).hexdigest()

    return hashed_login, hashed_password