import hmac
import hashlib
import base64
import json
import jwt
import time

from authentication.utils.decorators import secret_key

async def set_access_token(uuid, name):

    headers = {"alg": "HS256", "typ": "JWT"}
    payload = {"uuid": uuid, "name": name, "exp":  time.time() + 3600 * 3}


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