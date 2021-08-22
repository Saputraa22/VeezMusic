from time import time
from datetime import datetime
from config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, GROUP_SUPPORT
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helpers.decorators import authorized_users_only


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
    await message.reply_text(
        f"""<b>┗┓ Haii {message.from_user.first_name} ┏┛\n
Saya Bot Music Group, Yang dapat Memutar Lagu di Voice Chat Group Dengan cara yang Mudah

Saya Memiliki Banyak Fitur Praktis Seperti :
┏━━━━━━━━━━━━━━
┣• Memutar Musik.
┣• Mendownload Lagu.
┣• Mencari Lagu Yang DiInginkan.
┣• Daftar Perintah Lengkap » /help «
┗━━━━━━━━━━━━━━

❃ Owner bot : [ᴡᴀᴋᴀsᴀ](https://t.me/kibodisini)

━━━━━━━━━━━━━━━
Tambahkan saya ke grub anda..!!
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Tambahkan saya ke Grup Anda ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "☀️ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}")
                ],[
                    InlineKeyboardButton(
                        "⚡ ᴏᴡɴᴇʀ", url=f"https://t.me/kibodisini")
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""✅ **Bot sedang aktif**\n<b>💠 **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☀️ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{GROUP_SUPPORT}"
                    ),
                    InlineKeyboardButton(
                        "⚡ ᴏᴡɴᴇʀ", url=f"https://t.me/kibodisini"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hello {message.from_user.mention()}, silahkan tekan tombol dibawah untuk cara menggunakan bot ini</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="CARA MENGGUNAKAN❔", url=f"https://t.me/{BOT_USERNAME}?start=help"
                    )
                ]
            ]
        )
    )

@Client.on_message(command("help") & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hello {message.from_user.mention()}✨
\n📙 CARA MENGGUNAKAN BOT ?
\n1. Tambahkan bot ke grub/channel anda.
2. Jadikan bot sebagai admin.
3. Tambahkan @{ASSISTANT_NAME} di grub anda atau ketik /userbotjoin.
3. Pastikan obrolan suara sudah dinyalakan sebelum memutar music.
\n💁🏻‍♀️ **Perintah untuk semua member:**
\n/play (judul lagu) - memutar musik melalui youtube
/stream (balas ke audio) - memutar musik melalui file audio
/playlist - kenunjukan daftar putar
/current - menunjukan yang sedang diputar saat ini
/song (judul lagu) - mengunduh musik melalui youtube
/search (nama video) - mencari video dari youtube secara rinci
/vsong (nama video) - mengunduh video dari youtube secara rinci
/vk (judul lagu) - unduh melalui mode inline
\n👷🏻‍♂️ **Perinrah untuk admin:**
\n/player - membuka panel pengaturan musik
/pause - jeda pemutaran musik
/resume - melanjutkan pemutaran musik
/skip - melompati lagu yang sedang diputar
/end - menghentikan musik
/userbotjoin - mengundang assisten ke grup anda
/reload - untuk memperbarui daftar admin
/cache - untuk membersihkan cache admin
/musicplayer (on / off) - mematikan/menghidupkan pemutar musik di grupmu
\n🎧 Perintah untuk channel:
\n/cplay - mendengarkan musik lewat channel
/cplayer - melihat daftar putar
/cpause - jeda pemutar musik
/cresume - melajutkan musik yang di jeda
/cskip - melompati lagu yang sedang diputar
/cend - menghentikan lagu
/admincache - memperbarui cache admin
\n🧙‍♂️ Perintah sudo users:
\n/userbotleaveall - mengeluarkan asisten dari semua grup
/gcast - mengirim pesan siaran
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "☀️ ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/{UPDATES_CHANNEL}"), 
                    InlineKeyboardButton(
                        "✨ ɢʀᴏᴜᴘ", url=f"https://t.me/{GROUP_SUPPORT}")
                ],
                [
                    InlineKeyboardButton(
                        "👩🏻‍💻 ᴅᴇᴠᴇʟᴏᴘᴇʀ", url=f"https://t.me/kibodisini"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🏓 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@authorized_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "🤖 Bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
