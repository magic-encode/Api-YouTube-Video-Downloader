from rest_framework import status
from rest_framework.exceptions import APIException


class ServiceAPIException(APIException):
    def __init__(self, type, message, status_code=status.HTTP_400_BAD_REQUEST):
        self.status_code = status_code
        self.default_detail = {
            "error": {
                "type": type,
                "message": message
            }
        }
        super().__init__()
