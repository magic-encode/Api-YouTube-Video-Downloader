from django.urls import path

from .views import DownloaderAPIView


urlpatterns = [
    path('send-video/', DownloaderAPIView.as_view())
]
