# api_code/api/util.py
from datetime import datetime, timedelta, timezone
from typing import Optional

import jwt
from jwt.exceptions import PyJWTError

from .deps import Settings

ALGORITHM = "HS256"


class InvalidToken(Exception):
    pass


def create_token(payload: dict, key: str):
    now = datetime.now(tz=timezone.utc)
    data = {
        "iat": now,
        "exp": now + timedelta(hours=24),
        **payload,
    }
    return jwt.encode(data, key, algorithm=ALGORITHM)


def extract_payload(token: str, key: str):
    try:
        return jwt.decode(token, key, algorithms=[ALGORITHM])
    except PyJWTError as err:
        raise InvalidToken(str(err))


def is_admin(
    settings: Settings, authorization: Optional[str] = None
):
    if authorization is None:
        return False

    partition_key = (
        "Bearer" if "Bearer" in authorization else "bearer"
    )

    *dontcare, token = authorization.partition(
        f"{partition_key} "
    )
    token = token.strip()

    try:
        payload = extract_payload(token, settings.secret_key)
    except InvalidToken:
        return False
    else:
        return payload.get("role") == "admin"
