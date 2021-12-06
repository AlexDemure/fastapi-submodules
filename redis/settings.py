import os
from typing import Optional

from aiocache import Cache
from aiocache.serializers import PickleSerializer
from pydantic import BaseSettings, RedisDsn, validator


class RedisSettings(BaseSettings):

    REDIS_HOST: str = os.environ.get("REDIS_HOST", "localhost")
    REDIS_PORT: str = os.environ.get("REDIS_PORT", "6379")
    REDIS_DB: str = os.environ.get("REDIS_DB", "0")
    REDIS_PASSWORD: str = os.environ.get("REDIS_PASSWORD", "foobared")
    REDIS_URI: Optional[RedisDsn] = None

    @validator('REDIS_URI', pre=True)
    def assemble_redis_connection(cls, val: Optional[str], values) -> str:
        if isinstance(val, str):
            return val

        return RedisDsn.build(
            scheme="redis",
            host=values["REDIS_HOST"],
            port=values["REDIS_PORT"],
            path=f"/{values['REDIS_DB']}",
        )

    DEFAULT_CACHE_TTL = 60 * 30
    DEFAULT_CACHE_PARAMS = dict(
        cache=Cache.REDIS,
        serializer=PickleSerializer(),
        port=REDIS_PORT,
        password=REDIS_PASSWORD
    )
