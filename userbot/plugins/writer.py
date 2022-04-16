import os

from htmlwebshot import WebShot
from PIL import Image, ImageDraw, ImageFont

from ..helpers.tools import async_searcher, text_set
from . import legend

menu_category = "extra"


@legend.legend_cmd(
    pattern="gethtml(?:\s|$)([\s\S]*)",
    command=("gethtml", menu_category),
    info={
        "header": "text or reply to html or any doc file",
        "usage": "{tr}gethtml",
    },
)
async def ghtml(e):
    txt = e.text()
    link = txt[8:]
    k = await async_searcher(link)
    with open("file.html", "w+") as f:
        f.write(k)
    await e.reply(file="file.html")


@legend.legend_cmd(
    pattern="imagess(?:\s|$)([\s\S]*)",
    command=("imagess", menu_category),
    info={
        "header": "Write a image from html or any text",
        "usage": "{tr}imagess",
    },
)
async def f2i(e):
    lol = e.text
    html = None
    if e.reply_to:
        r = await e.get_reply_message()
        if r.media:
            html = await e.client.download_media(r.media)
        elif r.text:
            html = r.text
    elif lol:
        html = lol[7:]
    if not html:
        return await eod(e, "`Either reply to any file or give any text`")
    html = html.replace("\n", "<br>")
    shot = WebShot(quality=85)
    css = "body {background: white;} p {color: red;}"
    pic = await shot.create_pic_async(html=html, css=css)
    await e.reply(file=pic, force_document=True)
    os.remove(pic)
    if os.path.exists(html):
        os.remove(html)


@legend.legend_cmd(
    pattern="write(?:\s|$)([\s\S]*)",
    command=("write", menu_category),
    info={
        "header": "It will write on a paper.",
        "usage": "{tr}write",
    },
)
async def writer(e):
    lol = e.text
    if e.reply_to_msg_id:
        reply = await e.get_reply_message()
        text = reply.message
    elif lol:
        text = lol[6:]
    else:
        return await eod(e, "Give me Text")
    k = await eor(e, "Processing")
    img = Image.open("userbot/resources/extras/template.jpg")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("userbot/resources/fonts/assfont.ttf", 30)
    x, y = 150, 140
    lines = text_set(text)
    line_height = font.getsize("hg")[1]
    for line in lines:
        draw.text((x, y), line, fill=(1, 22, 55), font=font)
        y = y + line_height - 5
    file = "legend.jpg"
    img.save(file)
    await e.reply(file=file)
    os.remove(file)
    await k.delete()
