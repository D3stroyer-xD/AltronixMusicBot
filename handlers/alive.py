import asyncio
from time import time
from datetime import datetime
from modules.config import BOT_USERNAME
from modules.helpers.filters import command
from modules.helpers.command import commandpro
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)
    
   

@Client.on_message(command("start") & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d5ea5c258b4d8842f834f.jpg",
        caption=f"""**━━━━━━━━━━━━━━━━━━━━━━━━
💥 𝐻𝑒𝑙𝑙𝑜 𝐼'𝑚 𝑆𝑢𝑝𝑒𝑟 𝐹𝑎𝑠𝑡 𝑀𝑢𝑠𝑖𝑐 𝑃𝑙𝑎𝑦𝑒𝑟
𝐵𝑜𝑡 𝑓𝑜𝑟 𝑇𝑒𝑙𝑒𝑔𝑟𝑎𝑚 𝐺𝑟𝑜𝑢𝑝𝑠 ...
┏━━━━━━━━━━━━━━━━━┓
┣★ ⚡𝐶ℎ𝑎𝑛𝑛𝑒𝑙⚡ : [𝐴𝑙𝑡𝑟𝑜𝑛𝑖𝑥 𝐵𝑜𝑡𝑠](https://t.me/AltronixBots)
┣★ ⚡𝑆𝑢𝑝𝑝𝑜𝑟𝑡⚡ : [𝐴𝑙𝑡𝑟𝑜𝑛𝑖𝑥 𝑆𝑢𝑝𝑝𝑜𝑟𝑡](https://t.me/AltronixSupport)
┣★ ⚡𝑂𝑤𝑛𝑒𝑟⚡   : [𝐻𝑎𝑟𝑟𝑦](https://t.me/itz_harry_xD)
┗━━━━━━━━━━━━━━━━━┛
━━━━━━━━━━━━━━━━━━━━━━━━**""",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡ ❰ 𝗔𝗱𝗱 𝗠𝗲 𝗜𝗻 𝗚𝗿𝗼𝘂𝗽 ❱ ⚡", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ]
                
           ]
        ),
    )
    
    
@Client.on_message(commandpro(["/start", "/alive", "Altronix"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d5ea5c258b4d8842f834f.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝗦𝘂𝗽𝗽𝗼𝗿𝘁⚡", url=f"https://t.me/AltronixSupport")
                ]
            ]
        ),
    )


@Client.on_message(commandpro([".channel","toxic", "#Channel", "@Channel", "/Channel", "Channel"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/f3f2190d990196576a9c0.jpg",
        caption=f"""""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚡𝗖𝗵𝗮𝗻𝗻𝗲𝗹⚡", url=f"https://t.me/AltronixBots")
                ]
            ]
        ),
    )
