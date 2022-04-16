from telethon.tl.functions.channels import GetFullChannelRequest as getchat
from telethon.tl.functions.phone import CreateGroupCallRequest as startvc
from telethon.tl.functions.phone import DiscardGroupCallRequest as stopvc
from telethon.tl.functions.phone import EditGroupCallTitleRequest as settitle
from telethon.tl.functions.phone import GetGroupCallRequest as getvc
from telethon.tl.functions.phone import InviteToGroupCallRequest as invitetovc

from userbot import legend

from ..core.logger import logging
from ..core.managers import eod, eor

LOGS = logging.getLogger(__name__)
menu_category = "utils"


async def get_call(event):
    mm = await event.client(getchat(event.chat_id))
    xx = await event.client(getvc(mm.full_chat.call, limit=1))
    return xx.call


def user_list(l, n):
    for i in range(0, len(l), n):
        yield l[i : i + n]


@legend.legend_cmd(
    pattern="invitevc$",
    command=("invitevc", menu_category),
    info={
        "header": "Invite All To Vc",
        "description": "This Cmd  Is Used To Invite All Members Of Group In Voice Call",
        "usage": [
            "{tr}invitevc",
        ],
    },
    groups_only=True,
)
async def _(e):
    ok = await eor(e, "`Inviting Members to Voice Chat...`")
    users = []
    z = 0
    async for x in e.client.iter_participants(e.chat_id):
        if not x.bot:
            users.append(x.id)
    hmm = list(user_list(users, 6))
    for p in hmm:
        try:
            await e.client(invitetovc(call=await get_call(e), users=p))
            z += 6
        except BaseException:
            pass
    await ok.edit(f"`Invited {z} users`")


@legend.legend_cmd(
    pattern="stopvc$",
    command=("stopvc", menu_category),
    info={
        "header": "To Stop Vc",
        "description": "Use this cmd to stop voice call of the  Group",
        "usage": [
            "{tr}stopvc",
        ],
    },
    groups_only=True,
)
async def _(e):
    try:
        await e.client(stopvc(await get_call(e)))
        await eor(e, "`Voice Chat Stopped...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@legend.legend_cmd(
    pattern="playvc$",
    command=("playvc", menu_category),
    info={
        "header": "Soon It Will add Features",
        "description": "Comming Soon To Play Music In Group",
        "usage": [
            "{tr}playvc",
        ],
    },
    groups_only=True,
)
async def _(e):
    zz = await eor(e, "`VC bot started...`")
    er, out = await bash("python3 vcstarter.py & sleep 10 && npm start")
    LOGS.info(er)
    LOGS.info(out)
    if er:
        msg = f"Failed {er}\n\n{out}"
        if len(msg) > 4096:
            with open("vc-error.txt", "w") as f:
                f.write(msg.replace("`", ""))
            await e.reply(file="vc-error.txt")
            await zz.delete()
            remove("vc-error.txt")
            return
        await zz.edit(msg)


@legend.legend_cmd(
    pattern="startvc$",
    command=("startvc", menu_category),
    info={
        "header": "To start vc of the group",
        "description": "To start the voice call of group",
        "usage": [
            "{tr}startvc",
        ],
    },
    groups_only=True,
)
async def _(e):
    try:
        await e.client(startvc(e.chat_id))
        await eor(e, "`Voice Chat Started...`")
    except Exception as ex:
        await eor(e, f"`{str(ex)}`")


@legend.legend_cmd(
    pattern="vctitle(?:\s|$)([\s\S]*)",
    command=("vctitle", menu_category),
    info={
        "header": "To start vc of the group",
        "description": "To start the voice call of group",
        "usage": [
            "{tr}vctitle",
        ],
    },
    groups_only=True,
    require_admin=True,
)
async def _(e):
    title = e.pattern_match.group(1)
    if not title:
        return await eod(e, "Send Me Text of Title")
    try:
        await e.client(settitle(call=await get_call(e), title=title.strip()))
        await eod(e, "Done Voice call title changed")
    except Exception as ex:
        await e.eor(f"`{ex}`")
