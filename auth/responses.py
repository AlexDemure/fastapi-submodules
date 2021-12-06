from fastapi import status

responses = {
        status.HTTP_200_OK: {"description": "Access is allowed."},
        status.HTTP_401_UNAUTHORIZED: {"description": "Credentials is not validate."},
        status.HTTP_403_FORBIDDEN: {"description": "Forbidden."},
        status.HTTP_404_NOT_FOUND: {"description": "Sub is not found."}
}
