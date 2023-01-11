"""
MIT License

Copyright (c) 2022 Arsh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

from telethon import events, Button, custom
from Himawari.events import register
from Himawari import telethn as tbot, SUPPORT_CHAT, UPDATES_CHANNEL, BOT_NAME
HIMAWARI = "https://telegra.ph/file/9dfcdab5244a61b323210.jpg"
@register(pattern=("/alive"))
async def awake(event):
  STB = event.sender.first_name
  STB = f"**I am {BOT_NAME}** \n\n" + "**I am Working Properly**\n\n"
  STB += "**Python Version : 3.10.6**\n\n"
  STB += "**python-Telegram-Bot : 13.12**\n\n"
  BUTTON = [[Button.url("Support", "https://t.me/ENGLISH_SPEAKERSSS"), Button.url("Updates", "https://t.me/Baka_forum")]]
  await tbot.send_file(event.chat_id, HIMAWARI, caption=STB,  buttons=BUTTON)

  # thanks to stb the gay
