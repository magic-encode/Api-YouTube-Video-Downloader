from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_500_INTERNAL_SERVER_ERROR

from core.tasks import download
from core.errors.exceptions import ServiceAPIException


class DownloaderAPIView(APIView):
    def post(self, request):
        try:
            data = self.request.data
            download.delay(
                data.get('youtube_link'),
                data.get('chat_id'),
                data.get('message_id')
            )
        except Exception as error:
            raise ServiceAPIException(
                type=HTTP_500_INTERNAL_SERVER_ERROR,
                message="Error was occurred: {error}".format(
                    error=error
                )
            )
        return Response()
