import logging

from pyrogram import Client

# from pyromod import listen
from HexzyBot.conf import get_int_key, get_str_key

TOKEN = get_str_key("TOKEN", required=True)
API_ID = get_int_key("API_ID", required=True)
API_HASH = get_str_key("API_HASH", required=True)
session_name = TOKEN.split(":")[0]
Hxy = Client(
    session_name,
    api_id=APP_ID,
    api_hash=APP_HASH,
    bot_token=TOKEN,
)

# disable logging for pyrogram [not for ERROR logging]
logging.getLogger("pyrogram").setLevel(level=logging.ERROR)

Hxy.start()