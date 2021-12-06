import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware

from .settings import SENTRY_ACCESS_KEY


class SentrySDK:

    @staticmethod
    def senty_init(app):
        """Инициализация сервиса sentry."""
        sentry_sdk.init(
            dsn=SENTRY_ACCESS_KEY,
            # Sample rate - частота отправки ошибок в %. Максимальное значение 1.0.
            # Если одна и таже ошибка будет повторяться, тогда sentry будет отправлять только каждую четвертую ошибку.
            # Документацией рекомендуется начинать с значения 0.25 и увеличивать при необходимости.
            sample_rate=0.25,
        )
        SentryAsgiMiddleware(app=app)

    @staticmethod
    async def send_data(request, exception, **kwargs) -> None:
        """Конфигурирует и отправляет данные об ошибках и исключениях в sentry."""
        with sentry_sdk.push_scope() as scope:
            scope.set_context("request", request)
            scope.user = dict(ip_address=request.client.host, **kwargs)
            sentry_sdk.capture_exception(exception)


sentry = SentrySDK()
