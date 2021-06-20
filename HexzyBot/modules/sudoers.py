"""
XIT License 2021

Copyright (c) 2021 Prabhasha 


"""
import asyncio
import os
import subprocess
import time

from HexzyBot import (DEV_USERS, pbot)
import psutil
from pyrogram import filters

from HexzyBot import (bot_start_time, DEV_USERS, pbot)
from HexzyBot.utils import formatter


__MODULE__ = "Sudoers"
__HELP__ = """
/stats - To Check System Status.
/gstats - Comming Soon 
/gban - Comming Soon 
/broadcast - Comming Soon 
/update - Comming Soon 
"""

# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
root@Prabha_sha:~$ HexzyBot 
------------------
UPTIME: {formatter.get_readable_time((bot_uptime))}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
"""
    return stats

@pbot.on_message(
    filters.command("broadcast") & filters.user(DEV_USERS) & ~filters.edited
)
@capture_err
async def broadcast_message(_, message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage**:\n/broadcast [MESSAGE]")
    text = message.text.split(None, 1)[1]
    sent = 0
    chats = []
    schats = await get_served_chats()
    for chat in schats:
        chats.append(int(chat["chat_id"]))
    for i in chats:
        try:
            await app.send_message(i, text=text)
            sent += 1
        except Exception:
            pass
    await message.reply_text(f"**Broadcasted Message In {sent} Chats.**")
