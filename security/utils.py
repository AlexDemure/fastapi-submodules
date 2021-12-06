import random
import string
from typing import Optional

import itsdangerous.exc
from itsdangerous import URLSafeTimedSerializer
from pydantic import validate_arguments

from backend.core.config import settings

signer = URLSafeTimedSerializer(settings.SECRET_KEY)


@validate_arguments
def encode_token(context: dict) -> str:
    """Генерирование токена с помощью библиотеки ItsDangerous."""
    return signer.dumps(context)


@validate_arguments
def decode_token(token: str) -> Optional[dict]:
    """Проверка токена с помощью библиотеки ItsDangerous."""
    try:
        return signer.loads(token, max_age=settings.SECURITY_TOKEN_EXPIRE_SECONDS)
    except (itsdangerous.exc.SignatureExpired, itsdangerous.exc.BadSignature):
        return None


def generate_random_code(size=6, only_digits: bool = True):
    if only_digits:
        chars = string.digits
    else:
        chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))
