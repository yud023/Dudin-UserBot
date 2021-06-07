# gausah kesini ngentot!!

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.gjn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("Gajelas Ngentottt")


@register(outgoing=True, pattern='^.yb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Yabenarrrrrrr...**")


@register(outgoing=True, pattern='^.gjb(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAJELAS BABI....**")


@register(outgoing=True, pattern='^.gjk(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Gajelas Kontolll....**")


@register(outgoing=True, pattern='^.gbgn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**Ga banget, Ngentott!!!**")


@register(outgoing=True, pattern='^.gls(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK, LO SANGEAN!!!**")

CMD_HELP.update({
    "bacot1":
    ".gjn\
\nUsage:\
\n\n.yb\
\nUsage:\
\n\n.gjb\
\nUsage:\
\n\n.gjk\
\nUsage:\
\n\n.gbgn\
\nUsage:\
\n\n.gls\
\nUsage:"
})
