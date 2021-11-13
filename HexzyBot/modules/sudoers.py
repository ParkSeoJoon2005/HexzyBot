"""
XIT License 2021

Copyright (c) 2021 Prabhasha 


"""
import asyncio
import os
import subprocess
import time

import psutil
from pyrogram import filters

from HexzyBot import (bot_start_time, DEV_USERS, pbot)
from HexzyBot.utils import formatter

__mod_name__ = "🤗Reserved"

__help__ = """
*Only for Group Owner And Dragons:*
 ❍ /stats - To Check System Status.
 ❍ /gstats - Comming Soon 
 ❍ /gban - Comming Soon 
 ❍ /broadcast - Comming Soon 
 ❍ /update - Comming Soon 
"""


# Stats Module


async def bot_sys_stats():
    bot_uptime = int(time.time() - bot_start_time)
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
                    Ⱥմɾօɾą
root@Boy_alone_in_universe:~$ The-Aurora-Project 
------------------
UPTIME: {formatter.get_readable_time((bot_uptime))}
BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
"""
    return stats


