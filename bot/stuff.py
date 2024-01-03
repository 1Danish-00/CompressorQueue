#    This file is part of the CompressorQueue distribution.
#    Copyright (c) 2021 Danish_00
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/1Danish-00/CompressorQueue/blob/main/License> .

from .worker import *


async def up(event):
    if not event.is_private:
        return
    stt = dt.now()
    msg = await event.reply("ping…")
    ed = dt.now()
    ms = (ed - stt).microseconds / 1000
    p = f"🌋Pɪɴɢ = `{ms}ms"
    await msg.edit(p)


async def usage(event):
    if str(event.sender_id) not in OWNER:
        if event.sender_id != DEV:
            return
    total, used, free = shutil.disk_usage(".")
    cpuUsage = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    upload = hbs(psutil.net_io_counters().bytes_sent)
    down = hbs(psutil.net_io_counters().bytes_recv)
    TOTAL = hbs(total)
    USED = hbs(used)
    FREE = hbs(free)
    await event.reply(
        "**TOTAL DISK SPACE**: `{}`\n**USED**: `{}`\n**FREE**: {}\n**UPLOAD**: `{}`\n**DOWNLOAD**: `{}`\n**CPU**: `{}%`\n**RAM**: `{}%`\n**DISK**: `{}%`".format(
            TOTAL,
            USED,
            FREE,
            upload,
            down,
            cpuUsage,
            memory,
            disk,
        )
    )


async def start(event):
    await event.reply(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorQueue Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="github.com/1Danish-00/"),
                Button.url("DEVELOPER", url="t.me/danish_00"),
            ],
        ],
    )


async def help(event):
    await event.reply(
        "**🐠 A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options"
    )


async def ihelp(event):
    await event.edit(
        "**🐠 A Quality CompressorQueue**\n\n+This Bot Compress Videos With Negligible Quality Change.\n+Generate Sample Compressed Video\n+Screenshots Too\n+Easy to Use\n-Due to Quality Settings Bot Takes Time To Compress.\nSo Be patience Nd Send videos One By One After Completing.\nDont Spam Bot.\n\nJust Forward Video To Get Options",
        buttons=[Button.inline("BACK", data="beck")],
    )


async def beck(event):
    await event.edit(
        f"Hi `{event.sender.first_name}`\nThis is A CompressorQueue Which Can Encode Videos.\nReduce Size of Videos With Negligible Quality Change\nU can Generate Samples/screenshots too.",
        buttons=[
            [Button.inline("HELP", data="ihelp")],
            [
                Button.url("SOURCE CODE", url="github.com/1Danish-00/"),
                Button.url("DEVELOPER", url="t.me/danish_00"),
            ],
        ],
    )
