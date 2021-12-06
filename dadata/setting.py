import os

from pydantic import BaseSettings


class DaDataSetting(BaseSettings):

    DADATA_AUTH_TOKEN: str = os.environ.get("DADATA_AUTH_TOKEN", "58a19c749fe6752b903988083d85619ed191eec0")
