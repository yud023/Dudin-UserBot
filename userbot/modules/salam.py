from time import sleep
from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamu'alaikum NGENTOD`")
# Owner @Si_Dian
# Thanks XBOT-REMIX

@register(outgoing=True, pattern='^p(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**Hallo Semua Saya {DEFAULTUSER}**")
    sleep(2)
    await typew.edit("`Assalamu'alaikum NGENTOD`")
# Owner @Si_Dian
# Izin Maling Om

@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**{DEFAULTUSER} mengucapkan**")
    sleep(1)
    await typew.edit("`Wa'alaikumssalam YATI`")
# Owner @Si_Dian
# Izin Maling Om

@register(outgoing=True, pattern='^l(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit(f"**{DEFAULTUSER} mengucapkan**")
    sleep(1)
    await typew.edit("`Wa'alaikumssalam YATIM`")
# Owner @Si_Dian
# Izin Maling Om
# Hehehehe

CMD_HELP.update({
    "salam":
    "`P`\
\nUsage: Untuk Memberi salam.\
\n\n`L`\
\nUsage: Untuk Menjawab Salam."
})
