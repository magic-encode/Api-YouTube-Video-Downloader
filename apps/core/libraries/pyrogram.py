from pyrogram.client import Client

from mysite.settings import CREDENTIALS


app = Client(
    "prod_mode",
    api_id=CREDENTIALS.get('pyrogram').get('api_id'),
    api_hash=CREDENTIALS.get('pyrogram').get('api_hash'),
    bot_token=CREDENTIALS.get('pyrogram').get('bot_token'),
)
