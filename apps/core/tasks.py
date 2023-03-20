import logging

from mysite.celery import app

from youtube.libraries.youtube import youtube


logger = logging.getLogger(__name__)


@app.task(bind=True, max_retries=10, retry_delay=10)
def download(self, youtube_link: str, chat_id: str, message_id: int = None):
    try:
        youtube.downloader(
            youtube_link=youtube_link,
            chat_id=chat_id,
            message_id=message_id
        )
    except Exception as exc:
        logger.error("error while downloading video image: {exc}".format(
            exc=exc
        ))
        raise self.retry(exc=exc, countdown=1)
