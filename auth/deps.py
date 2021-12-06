from typing import Optional
from fastapi import Depends, Body
from fastapi.security import OAuth2PasswordBearer

from backend.core.config import settings
from .enums import TokenPurpose
from .errors import AuthError
from .schemas import RefreshTokenParams
from .security import decode_token

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.API_URL}{settings.AUTH_ACCESS_URL}")


def get_subject_from_auth_token(token: str = Depends(reusable_oauth2)) -> Optional[int]:
    """Получение объекта из авторизационного токена."""
    try:
        token_payload = decode_token(token, TokenPurpose.access)
    except AuthError:
        return None

    return int(token_payload.sub)


def get_subject_from_refresh_token(params: RefreshTokenParams = Body(...)) -> Optional[int]:
    """Получение объекта из refresh токена."""
    try:
        token_payload = decode_token(params.token, TokenPurpose.refresh)
    except AuthError:
        return None

    return int(token_payload.sub)
