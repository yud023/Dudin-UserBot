# Credits By @VckyouuBitch From Geez-Project
# Tolong Haragai ya:)
# Kalo emg Bisa Menghargai seseorang pasti pahamm la ya:)
# Credits © Geez - Projects

import os
from datetime import datetime as dt
from random import choice
from shutil import rmtree

import moviepy.editor as m
import pytz
import requests
from bs4 import BeautifulSoup as b

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.getaudio(?: |$)(.*)")
async def daudtoid(event):


@register(outgoing=True, pattern="^.getaudio(?: |$)(.*)", disable_errors=True)
async def _(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("audio" in ureply.document.mime_type)):
        await event.edit("`Reply To Audio Only..`")


@ @ -25, 8 + 24, 8 @ @ async def daudtoid(event):
    await event.edit("`Done.. Now reply to video In which u want to add that Audio`")


@register(outgoing=True, pattern="^.addaudio(?: |$)(.*)")
async def adaudroid(event):


@register(outgoing=True, pattern="^.addaudio(?: |$)(.*)", disable_errors=True)
async def _(event):
    ureply = await event.get_reply_message()
    if not (ureply and ("video" in ureply.document.mime_type)):
        await event.edit("`Reply To Gif/Video In which u want to add audio.`")


@ @ -54, 7 + 53, 6 @ @ async def adaudroid(event):
    os.remove(ultt)
    await xx.delete()


CMD_HELP.update(
    {
        "specialtools": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.getaudio`\
