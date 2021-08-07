from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎀
I Cᴀɴ Pʟᴀʏ Mᴜsɪᴄ Iɴ Yᴏᴜʀ Sᴇxʏ Gʀᴏᴜᴩ Vᴏɪᴄᴇ Cʜᴀᴛ. Dᴇᴠᴇʟᴏᴩᴇᴅ Bʏ [ƧΣXY BӨY](https://t.me/Xd_Lif).
Aᴅᴅ Mᴇ Tᴏ Yᴏᴜʀ Gʀᴏᴜᴩ Aɴᴅ Pʟᴀʏ Mᴜsɪᴄ Fʀᴇᴇʟʏ!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Lᴇᴀɢɴᴅ🦋", url="t.me/aish_jaan_0")
                  ],[
                    InlineKeyboardButton(
                        "Mᴜsɪᴄ 👿", url="https://t.me/LOVExWORD"
                    ),
                    InlineKeyboardButton(
                        "Cʜᴀɴɴᴇʟ", url="https://t.me/LXW_UPDATE"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Kᴀʀʟᴏ Aʙʙ Aᴅᴅ ➕", url="https://t.me/innexiaMusicRoBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Aᴍ Oɴʟɪɴᴇ ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "👻Uᴩᴅᴀᴛᴇs", url="https://t.me/LXW_UPDATE")
                ]
            ]
        )
   )
