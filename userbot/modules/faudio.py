@register(outgoing=True, pattern="^.faudio(?: |$)(.*)")
async def _(e):
    t = e.pattern_match.group(1)
    if not (t or t.isdigit()):
        t = 100
    else:
        try:
            t = int(t)
        except BaseException:
            try:
                t = await ban_time(e, t)
            except BaseException:
                return await eod(e, "`Incorrect Format`")
    await eod(e, f"Starting Fake audio recording For {t} sec.")
    async with e.client.action(e.chat_id, "record-audio"):
        await asyncio.sleep(t)
