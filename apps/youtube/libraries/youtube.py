import os
import logging

from pytube import YouTube

from mysite.settings import CREDENTIALS

from core.models import Videos

from core.libraries.pyrogram import app
from core.libraries.inline import share_button

from pyrogram.types import InlineKeyboardMarkup


logger = logging.getLogger(__name__)


class YoutubeDownloader:

    def downloader(self, youtube_link: str, chat_id: str, message_id: int = None) -> str: # noqa
        """
        Youtube downloader method that helps to download youtube videos
        using the given youtube link.
        param: youtube_link -> str youtube video link for downloading
        """
        try:
            yt = YouTube(youtube_link)
            file_path = yt.streams\
                .filter(progressive=True, file_extension='mp4')\
                .order_by('resolution')\
                .desc()\
                .first()\
                .download()

            file_id = self.check_in_db(
                youtube_link=youtube_link
            )
            if file_id is None:
                with open(file_path, "rb") as file:
                    message = app.send_video(
                        chat_id=chat_id,
                        video=file,
                        caption="Video by {bot_name}".format(
                            bot_name=CREDENTIALS.get('pyrogram').get('bot_name') # noqa
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[[share_button(
                                text="Share Me"
                            )]]
                        )
                    )
                    os.remove(file_path)

                    self.check_in_db(
                        youtube_link=youtube_link,
                        file_id=message.video.file_id,
                        chat_id=chat_id,
                    )

            if file_id is not None:
                with app:
                    try:
                        app.delete_messages(
                            chat_id=int(chat_id),
                            message_ids=int(message_id)
                        )
                    except Exception as error:
                        logger.error(error)

                    app.send_video(
                        chat_id=chat_id,
                        video=file_id,
                        caption="Video by {bot_name}".format(
                            bot_name=CREDENTIALS.get('pyrogram').get('bot_name') # noqa
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            inline_keyboard=[[share_button(
                                text="Share Me"
                            )]]
                        )
                    )
                    return

        except ConnectionResetError as error:
            logger.error("error while downloading video: {youtube_link}, error: {error}".format( # noqa
                youtube_link=youtube_link,
                error=error
            ))
            raise ConnectionResetError()

    @staticmethod
    def check_in_db(
        youtube_link: str,
        file_id: int = None,
        chat_id: int = None
    ):
        try:
            video: Videos = Videos.objects.get(
                youtube_link=youtube_link
            )
            if video.file_id:
                return video.file_id

        except Videos.DoesNotExist:
            if file_id:
                Videos.objects.create(
                    youtube_link=youtube_link,
                    file_id=file_id
                )

        except Exception as error:
            logger.error("Error was occurred while using video filter method: {error}".format( # noqa
                error=error
            ))


youtube = YoutubeDownloader()
