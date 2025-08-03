from hashlib import sha256


async def hash_password(password):

    hashed_password = sha256(password.encode('utf-8')).hexdigest()

    return hashed_password