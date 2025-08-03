import hmac
import hashlib
import base64
import json
import jwt
from fastapi import HTTPException
import time
import asyncio

from config.getter import secret_key

async def set_access_token(id):

    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {"id": id, "exp": time.time() + 3600 * 3}


    encoded_headers = base64.urlsafe_b64encode(json.dumps(headers).encode('utf-8')).decode('utf-8').rstrip("=")
    encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8').rstrip("=")

    data_to_sign = f"{encoded_headers}.{encoded_payload}".encode('utf-8')

    signature = hmac.new(
        secret_key.encode('utf-8'),
        data_to_sign,
        hashlib.sha256
    ).digest()

    encoded_signature = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip("=")

    jwt_token = f"{encoded_headers}.{encoded_payload}.{encoded_signature}"

    return jwt_token

async def set_refresh_token(id):

    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {"id": id, "exp": time.time() + 3600 * 24 * 30}

    encoded_headers = base64.urlsafe_b64encode(json.dumps(headers).encode('utf-8')).decode('utf-8').rstrip("=")
    encoded_payload = base64.urlsafe_b64encode(json.dumps(payload).encode('utf-8')).decode('utf-8').rstrip("=")

    data_to_sign = f"{encoded_headers}.{encoded_payload}".encode('utf-8')

    signature = hmac.new(
        secret_key.encode('utf-8'),
        data_to_sign,
        hashlib.sha256
    ).digest()

    encoded_signature = base64.urlsafe_b64encode(signature).decode('utf-8').rstrip("=")

    jwt_token = f"{encoded_headers}.{encoded_payload}.{encoded_signature}"

    return jwt_token, await asyncio.create_task(set_access_token(id))


async def get_access_token(token, refresh_token):
    try:
        valid_token = jwt.decode(token, secret_key, algorithms=['HS256'])
    except:
        return HTTPException(401)
    if time.time() > valid_token['exp']:
        valid_token = await asyncio.create_task(get_refresh_token(valid_token['id'], refresh_token))
    return valid_token

async def get_refresh_token(id, refresh_token):

    refresh_token = jwt.decode(refresh_token, secret_key, algorithms=['HS256'])

    if time.time() > refresh_token['exp']:
        return HTTPException(401)

    return await asyncio.create_task(set_access_token(id))