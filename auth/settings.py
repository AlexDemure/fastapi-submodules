from pydantic import BaseSettings


class AuthSettings(BaseSettings):

    ALGORITHM = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 12  # 60 minutes * 12 hours = 0.5day
    REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 30  # 60 minutes * 24 hours = (1day) * 30 days = 30days

    AUTH_ACCESS_URL = "/login/access-token/"
    AUTH_REFRESH_URL = "/login/refresh-token/"
