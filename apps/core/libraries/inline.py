from pyrogram.types import InlineKeyboardButton
from pyrogram.types import InlineKeyboardMarkup


def share_button(text: str) -> InlineKeyboardMarkup:
    share_button = InlineKeyboardButton(
        text=text,
        switch_inline_query="YouTube Video Downloader"
    )
    return share_button
