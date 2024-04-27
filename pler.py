import os, logging, asyncio

import random
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from config import *

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
kntl = TelegramClient('kynan', api_id, api_hash).start(bot_token=bot_token)


spam_chats = []


@kntl.on(events.NewMessage(pattern="^/start$"))
async def help(event):
  helptext = "**𝘄𝗼𝘆 𝗶𝗻𝗶 𝗯𝗼𝘁 𝘁𝗮𝗴𝗮𝗹𝗹,𝗹𝘂 𝗸𝗮𝗹𝗼 𝗺𝗮𝘂 𝘁𝗮𝗴𝗮𝗹𝗹 𝗸𝗲𝘁𝗶𝗸 /all 𝗸𝗮𝗹𝗼 𝗺𝗮𝘂 𝘀𝘁𝗼𝗽𝗶𝗻 𝘁𝗮𝗴𝗮𝗹𝗹 𝗻𝘆𝗮 𝗸𝗲𝘁𝗶𝗸 /stop 𝗸𝗮𝗹𝗼 𝗽𝗹𝗮𝘆 𝗺𝘂𝘀𝗶𝗰 𝗸𝗲𝘁𝗶𝗸 /play (𝗷𝘂𝗱𝘂𝗹 𝗹𝗮𝗴𝘂) 𝗸𝗮𝗹𝗼 𝗴𝗮 𝗻𝘆𝗮𝘂𝘁 𝗻𝗴𝗮𝗱𝘂 𝗮𝗷𝗮 𝘀𝗮𝗺𝗮 𝗲𝘄𝗲 👇.**"
  await event.reply(
    helptext,
    link_preview=False,
    buttons=(
      [
        Button.url('𝗴𝘂𝗮𝗮', 't.me/rewe_anu'),
      ],
      [
        Button.url('𝗰𝗵 𝗴𝘂𝗮𝗮', 't.me/nunagabut2'),
        Button.url('𝘀𝘂𝗽𝗽𝗼𝗿𝘁 𝗴𝘂𝗮𝗮', 't.me/supprotrewe'),
      ],
    )
  )
  
@kntl.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("**𝗷𝗮𝗻𝗴𝗮𝗻 𝗽𝗿𝗶𝘃𝗮𝘁 𝗸𝗼𝗻𝘁𝗼𝗹**")
  
  is_admin = False
  try:
    partici_ = await kntl(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("**𝗹𝘂 𝗯𝘂𝗸𝗮𝗻 𝗮𝗱𝗺𝗶𝗻 𝘆𝗮 𝗮𝗻𝗷𝗴**")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("**𝗺𝗶𝗻𝗶𝗺𝗮𝗹 𝗸𝗮𝘀𝗶 𝗽𝗲𝘀𝗮𝗻 𝗶𝗱𝗶𝗼𝘁 𝗯𝗻𝗴𝗲𝘁 𝗯𝗼𝗰𝗮𝗵!!**")
  elif event.pattern_match.group(1):
    mode = "teks"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "balas"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("**𝘀𝗶 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 𝗸𝗼𝗻𝘁𝗼𝗹 𝘀𝗸𝘀𝗵𝗮𝗵𝘀𝗼𝘀𝘂𝗮𝗵𝗮 𝗴𝘂𝗮 𝗯𝗶𝗹𝗮𝗻𝗴 𝗸𝗮𝘀𝗶 𝗽𝗲𝘀𝗮𝗻 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 !!**")
  else:
    return await event.respond("**𝘀𝗶 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 𝗸𝗼𝗻𝘁𝗼𝗹 𝘀𝗸𝘀𝗵𝗮𝗵𝘀𝗼𝘀𝘂𝗮𝗵𝗮 𝗴𝘂𝗮 𝗯𝗶𝗹𝗮𝗻𝗴 𝗸𝗮𝘀𝗶 𝗽𝗲𝘀𝗮𝗻 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 !!**")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in kntl.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"👅 [{usr.first_name}](tg://user?id={usr.id})\n"
    if usrnum == 5:
      if mode == "teks":
        txt = f"{usrtxt}\n\n{msg}"
        await kntl.send_message(chat_id, txt)
      elif mode == "balas":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass


@kntl.on(events.NewMessage(pattern="^/stop$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('**𝗴𝗯𝗹𝗼𝗸 𝗼𝗿𝗮𝗻𝗴 𝗴𝗮𝗱𝗮 𝘁𝗮𝗴𝗮𝗹𝗹 𝗮𝗻𝗷**')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**𝗶𝘆𝗮 𝗮𝗻𝗷𝗴 𝗻𝗶 𝗴𝘂𝗮 𝘀𝘁𝗼𝗽𝗶𝗻.**')


@kntl.on(events.NewMessage(pattern="^/all ?(.*)"))
async def mentionall(event):
  chat_id = event.chat_id
  if event.is_private:
    return await event.respond("**𝗷𝗮𝗻𝗴𝗮𝗻 𝗽𝗿𝗶𝘃𝗮𝘁 𝗸𝗼𝗻𝘁𝗼𝗹**")
  
  is_admin = False
  try:
    partici_ = await kntl(GetParticipantRequest(
      event.chat_id,
      event.sender_id
    ))
  except UserNotParticipantError:
    is_admin = False
  else:
    if (
      isinstance(
        partici_.participant,
        (
          ChannelParticipantAdmin,
          ChannelParticipantCreator
        )
      )
    ):
      is_admin = True
  if not is_admin:
    return await event.respond("**𝗹𝘂 𝗯𝘂𝗸𝗮𝗻 𝗮𝗱𝗺𝗶𝗻 𝘆𝗮 𝗮𝗻𝗷𝗴**")
  
  if event.pattern_match.group(1) and event.is_reply:
    return await event.respond("**𝗺𝗶𝗻𝗶𝗺𝗮𝗹 𝗸𝗮𝘀𝗶 𝗽𝗲𝘀𝗮𝗻 𝗶𝗱𝗶𝗼𝘁 𝗯𝗻𝗴𝗲𝘁 𝗯𝗼𝗰𝗮𝗵!!**")
  elif event.pattern_match.group(1):
    mode = "teks"
    msg = event.pattern_match.group(1)
  elif event.is_reply:
    mode = "balas"
    msg = await event.get_reply_message()
    if msg == None:
        return await event.respond("**𝘀𝗶 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 𝗸𝗼𝗻𝘁𝗼𝗹 𝘀𝗸𝘀𝗵𝗮𝗵𝘀𝗼𝘀𝘂𝗮𝗵𝗮 𝗴𝘂𝗮 𝗯𝗶𝗹𝗮𝗻𝗴 𝗸𝗮𝘀𝗶 𝗽𝗲𝘀𝗮𝗻 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 !!**")
  else:
    return await event.respond("**𝘀𝗶 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 𝗸𝗼𝗻𝘁𝗼𝗹 𝘀𝗸𝘀𝗵𝗮𝗵𝘀𝗼𝘀𝘂𝗮𝗵𝗮 𝗴𝘂𝗮 𝗯𝗶𝗹𝗮𝗻𝗴 𝗸𝗮𝘀𝗶 𝗽𝗲𝘀𝗮𝗻 𝗮𝗻𝗷𝗴 𝗶𝗱𝗶𝗼𝘁 !!**")
  
  spam_chats.append(chat_id)
  usrnum = 0
  usrtxt = ''
  async for usr in kntl.iter_participants(chat_id):
    if not chat_id in spam_chats:
      break
    usrnum += 1
    usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id})"
    if usrnum == 5:
      if mode == "teks":
        txt = f"{usrtxt}\n\n{msg}"
        await kntl.send_message(chat_id, txt)
      elif mode == "balas":
        await msg.reply(usrtxt)
      await asyncio.sleep(2)
      usrnum = 0
      usrtxt = ''
  try:
    spam_chats.remove(chat_id)
  except:
    pass


print("BOT AKTIF YA IDIOT")
kntl.run_until_disconnected()
