import os
from decimal import Decimal
from pydantic import BaseSettings


class YandexObjectStorage(BaseSettings):

    YANDEX_ACCESS_KEY_ID: str = os.environ.get("YANDEX_ACCESS_KEY_ID", "NOT_SET")
    YANDEX_SECRET_ACCESS_KEY: str = os.environ.get("YANDEX_SECRET_ACCESS_KEY", "NOT_SET")
    YANDEX_BUCKET_NAME: str = os.environ.get("YANDEX_BUCKET_NAME", "bustail")


IMAGE_LIMIT_SIZE_TO_BYTES = Decimal(5 * 1024 * 1024)  # 5 MB
FILE_LIMIT_SIZE_TO_BYTES = Decimal(10 * 1024 * 1024)  # 10 MB