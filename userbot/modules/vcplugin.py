# Adudin
# Copyright (C) 2021 Geez Project
from userbot.events import register
from userbot import CMD_HELP
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc



async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i: i + n]


@register(outgoing=True, pattern=r"^\.vcinvite(?: |$)(.*)",
          disable_errors=True, groups_only=True)
async def _(event):
    await event.edit("`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for geez in event.client.iter_participants(event.chat_id):
        if not geez.bot:
            users.append(geez.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await event.client(invitetovc(call=await event.get_call, users=p))
            z += 6
        except BaseException:
            pass
    await event.edit(f"`Invited {z} users`")


CMD_HELP.update(
    {
        "vcplugin": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.vcjoin : .vcstop : .vcplay : .vcinvite : .fgame <jumlah text>`"
        "\n• : Fake typing ini Berfungsi dalam group"
    }
)
