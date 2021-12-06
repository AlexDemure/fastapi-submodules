from .enums import AuthErrors


class AuthError(BaseException):
    """
    Исключение в логике обработки материалов
    """
    def __init__(self, error_code: AuthErrors):
        self.error_code = error_code
