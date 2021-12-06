from fastapi import status

from .enums import BaseMessage

auth_responses = {
    status.HTTP_403_FORBIDDEN: {"description": BaseMessage.forbidden.value},
    status.HTTP_404_NOT_FOUND: {"description": BaseMessage.obj_is_not_found.value}
}
