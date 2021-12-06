from datetime import datetime, timedelta
from uuid import uuid4

from jose import jwt
from passlib.context import CryptContext
from pydantic import ValidationError, validate_arguments

from backend.core.config import settings
from .enums import TokenPurpose, AuthErrors
from .errors import AuthError
from .schemas import Token, TokenPayload

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def encode_token(**kwargs):
    return jwt.encode(kwargs, settings.SECRET_KEY, algorithm=settings.ALGORITHM)


@validate_arguments
def decode_token(token: str, token_purpose: TokenPurpose) -> TokenPayload:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenPayload(**payload)

        if token_data.purpose != token_purpose:
            raise AuthError(AuthErrors.purpose_is_wrong.value)

    except jwt.ExpiredSignatureError:
        raise AuthError(AuthErrors.token_is_expired.value)
    except (jwt.JWTError, ValidationError):
        raise AuthError(AuthErrors.tokes_is_wrong.value)

    return token_data


@validate_arguments
def generate_token(subject: str) -> Token:
    now = datetime.utcnow()
    jwt_identifier = str(uuid4())

    return Token(
        access_token=encode_token(
            sub=subject,
            purpose=TokenPurpose.access,
            exp=now + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
            jti=jwt_identifier
        ),
        refresh_token=encode_token(
            sub=subject,
            purpose=TokenPurpose.refresh,
            exp=now + timedelta(minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES),
            jti=jwt_identifier
        ),
    )


@validate_arguments
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


@validate_arguments
def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

