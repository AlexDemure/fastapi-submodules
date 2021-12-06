from pydantic import BaseSettings


class SecuritySettings(BaseSettings):

    SECURITY_TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24  # 60 seconds * 60 minute = 1(hr) * 24 = 1day
