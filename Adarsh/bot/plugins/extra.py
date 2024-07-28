from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime


START_TEXT = """ ʏᴏᴜʀ  ᴛᴇʟᴇɢʀᴀᴍ  ᴅᴄ  ɪꜱ : `{}`  """

      
     


    
@StreamBot.on_message(filters.command("list"))
async def list(l, m):
    LIST_MSG = " {},\nHere is a list of all my commands \n \n 1 . `Start⚡️` \n 2. `Help📚` \n 3.`Follow❤️` \n 4. `Ping📡` \n 5. `Status📊` \n 6. `Owner😎` "
    await l.send_message(chat_id = m.chat.id,
        text = LIST_MSG.format(m.from_user.mention(style="md"))
        
    )
    
    
@StreamBot.on_message(filters.regex("ping📡"))
async def ping(b, m):
    start_t = time.time()
    ag = await m.reply_text("....")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await ag.edit(f"ᴘᴏɴɢ\n{time_taken_s:.3f} ms")
    
    
    
    
@StreamBot.on_message(filters.private & filters.regex("status📊"))
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>⏳ ᴜᴘᴛɪᴍᴇ:</b> {currentTime}\n' \
            f'<b>♻️ ᴛᴏᴛᴀʟ:</b> {total}\n' \
            f'<b>🆓 ꜰʀᴇᴇ: </b> {free}\n' \
            f'<b>🉐 ᴏᴄᴄᴜᴘɪᴇᴅ:</b> {used} \n\n\n' \
            f'<b>📊  ᴅᴀᴛᴀ  ᴜꜱᴀɢᴇꜱ  📊</b>\n\n<b>☣️  ᴄᴘᴜ:</b> {cpuUsage}% \n' \
            f'<b>☢️  ʀᴀᴍ:</b> {memory}% \n' \
            f'<b>☣️  ᴅɪꜱᴋ:</b> {disk}% \n' \
            f'<b>📤  ᴜᴘʟᴏᴀᴅ:</b> {sent}\n' \
            f'<b>📥  ᴅᴏᴡɴ:</b> {recv}'
  await update.reply_text(botstats)
