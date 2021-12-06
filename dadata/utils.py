import httpx

from structlog import get_logger

from backend.enums.system import SystemEnvs
from backend.core.config import settings


class DaBase:

    endpoint_url = None
    auth_token = None

    logger = None

    def __init__(self):
        self.auth_token = settings.DADATA_AUTH_TOKEN
        self.logger = get_logger()

    async def send(self, data: dict) -> dict:
        async with httpx.AsyncClient() as client:
            if settings.ENV == SystemEnvs.prod.value:
                self.logger.debug("Send to DaData service", data=data)
                response = await client.post(
                    url=self.endpoint_url,
                    headers={
                        "Content-Type": 'application/json',
                        "Accept": 'application/json',
                        "Authorization": f"Token {self.auth_token}"
                    },
                    json=data,
                )
                assert response.status_code == 200, f"DaData bad response: {response.text}"
                self.logger.info(f'Message: {response}')

                json = response.json()
            else:
                self.logger.debug("Request is don't send to DaData")
                json = dict(
                    suggestions=[
                        dict(
                            value="Fake result",
                        )
                    ]
                )

        return json


class DaCompany(DaBase):

    endpoint_url = "https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party"

    async def find(self, query: str) -> tuple:
        """
        Поиск Юр.лица.
        Query - ИНН или ОГРН

        Возвращает результат и булевое значение найдены ли записи или нет.
        """
        is_find = False

        company = await self.send(dict(query=query))
        if len(company['suggestions']) > 0:
            is_find = True

        return company, is_find
