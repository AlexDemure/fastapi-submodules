from enum import Enum


class TokenPurpose(str, Enum):
    access = 'access'
    refresh = 'refresh'


class AuthErrors(Enum):
    token_is_expired = "Авторизационный токен истек. Необходима повторная авторизация."
    tokes_is_wrong = "В токене содержатся не корректные данные."
    purpose_is_wrong = "Не корректный тип токена."
