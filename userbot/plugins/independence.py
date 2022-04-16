import asyncio
import os
import random
import shutil
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.tl import functions

from .. import legend
from ..core.logger import logging
from ..core.managers import eor
from . import mention

menu_category = "useless"

LOGS = logging.getLogger(__name__)


@legend.legend_cmd(
    pattern="indanime(?:\s|$)([\s\S]*)",
    command=("indanime", menu_category),
    info={
        "header": "Wish Happy Independence Day",
        "description": "It Can Help U To Send Independence Day Message To All Group/user According to flags",
        "flags": {
            "-a": "To Send Independance Day All User & Group",
            "-g": "To Send Independance Day In All Group",
            "-p": "To Send Independance Day In All User",
        },
        "usage": [
            "{tr}indanime <type>",
        ],
        "examples": [
            "{tr}indanime -a",
        ],
    },
)
async def xd(event):
    "Help U To Send Independance Day Message In All Group & User"
    await event.get_reply_message()
    type = event.text[9:11] or "-a"
    hol = await eor(event, "`Sending Independance Day message...`")
    sed = 0
    lol = 0
    if type == "-a":
        async for aman in event.client.iter_dialogs():
            chat = aman.id
            try:
                if chat != -1001551357238:
                    await bot.send_message(
                        chat,
                        f"⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n[нαρργ ιи∂ρєи∂єиϲє ∂αγ🇮🇳](https://t.me/LegendBot_OP)",
                    )
                    lol += 1
                elif chat == -1001551357238:
                    pass
            except BaseException:
                sed += 1
    elif type == "-p":
        async for krishna in event.client.iter_dialogs():
            if krishna.is_user and not krishna.entity.bot:
                chat = krishna.id
                try:
                    await bot.send_message(
                        chat,
                        f"⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n[нαρργ ιи∂ρєи∂єиϲє ∂αγ🇮🇳](https://t.me/LegendBot_OP)",
                    )
                    lol += 1
                except BaseException:
                    sed += 1
    elif type == "-g":
        async for sweetie in event.client.iter_dialogs():
            if sweetie.is_group:
                chat = sweetie.id
                try:
                    if chat != -1001551357238:
                        await bot.send_message(
                            chat,
                            f"⣿⣿⣿⣿⣿⣍⠀⠉⠻⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⠓⠀⠀⢒⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿\n⣿⡿⠋⠋⠀⠀⠀⠀⠀⠀⠈⠙⠻⢿⢿⣿⣿⡿⣿⣿⡟⠋⠀⢀⣩\n⣿⣿⡄⠀⠀⠀⠀⠀⠁⡀⠀⠀⠀⠀⠈⠉⠛⢷⣭⠉⠁⠀⠀⣿⣿\n⣇⣀. INDIA🇮🇳INDIA🇮🇳⠆⠠..⠘⢷⣿⣿⣛⠐⣶⣿⣿\n⣿⣄⠀⣰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢀⣠⣿⣿⣿⣾⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⡠⠀⠀⠀⠀⠀⢀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠄⠀⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⠀⠀⠂⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣇⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⡆⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⣿⣿⣿⣿⣿⣿⣿⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\n[нαρργ ιи∂ρєи∂єиϲє ∂αγ🇮🇳](https://t.me/LegendBot_OP)",
                        )
                        lol += 1
                    elif chat == -1001551357238:
                        pass
                except BaseException:
                    sed += 1
    else:
        return await hol.edit(
            "Please give a flag to Send Independence Day Message. \n\n**Available flags are :** \n• -a : To send Good  Afternoon in all chats. \n• -p : To Send Good Afternoon in private chats. \n• -g : To Send Good Afternoon in groups."
        )
    UwU = sed + lol
    if type == "-a":
        omk = "Chats"
    elif type == "-p":
        omk = "PM"
    elif type == "-g":
        omk = "Groups"
    await hol.edit(
        f"**Independence Message Executed Successfully !!** \n\n** Sent in :** `{lol} {omk}`\n**📍 Failed in :** `{sed} {omk}`\n**📍 Total :** `{UwU} {omk}`"
    )


@legend.legend_cmd(
    pattern="independence(?:\s|$)([\s\S]*)",
    command=("independence", menu_category),
    info={
        "header": "Wish Happy Independence Day",
        "description": "It Can Help U To Send Independence Day Message ",
        "usage": [
            "{tr}independence",
        ],
    },
)
async def _(event):
    animation_interval = 6
    animation_ttl = range(0, 17)
    await event.edit("Starting...")
    animation_chars = [
        "**нєℓℓο!👋**",
        "**нοω αяє υ?**",
        f"**{mention} : нαρργ ιи∂єρєи∂єиϲє ∂αγ**",
        "ωιѕнιиg υ нαρργ ιи∂єρєи∂єиϲє ∂αγ",
        "**Happy 😊 Indpendence Day!**",
        "**From every mountain side Let Fredom Ring**",
        "**Independence means.. enjoying freedom and empowering others too to let them do so.**",
        "ͲϴᎠᎪᎽ ᏔᎬ ᎪᎡᎬ ҒᎡᎬᎬ ᏴᎬᏟᎪႮՏᎬ ᎷᎪΝᎽ ՏᎪᏟᎡᏆҒᏆᏟᎬᎠ ͲᎻᎬᎡᎬ ᏞᏆᏙᎬՏ ҒϴᎡ ᏆΝᎠᏆᎪ \nՏᎪᏞႮͲᎬ ͲᎻᎬ ᏀᎡᎬᎪͲ ՏϴႮᏞՏ",
        "[ƒοя υ](https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg)",
        "[нαρργ ιи∂ρєи∂єиϲє ∂αγ](https://t.me/Legend_Userbot)",
    ]
    for i in animation_ttl:  # By @The_LegendBoy LegendBot

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 17], link_preview=True)


FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

# Add telegraph media links of profile pics that are to be used
TELEGRAPH_MEDIA_LINKS = [
    "https://telegra.ph/file/a2b6e3781680a6d85f842.jpg",
    "https://telegra.ph/file/2f2035b4e8ab1dc6efc3d.jpg",
    "https://telegra.ph/file/18e4d7c45e49ad9340e3c.jpg",
    "https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg",
    "https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg",
    "https://telegra.ph/file/66205f168d8c2a0bbaa43.jpg",
    "https://telegra.ph/file/3072bb5fd2c8dd8e9da60.jpg",
    "https://telegra.ph/file/24f84ab213b177ef43d6e.jpg",
    "https://telegra.ph/file/bc96df71964af1a4ac625.jpg",
    "https://telegra.ph/file/bc96df71964af1a4ac625.jpg",
    "https://telegra.ph/file/bc96df71964af1a4ac625.jpg",
]


@legend.legend_cmd(
    pattern="inddp(?:\s|$)([\s\S]*)",
    command=("inddp", menu_category),
    info={
        "header": "To Apply Automatically Dp ",
        "description": "Automatically Auto Dp Apply On profile Pic",
        "usage": [
            "{tr}inddp",
        ],
    },
)
async def autopic(event):
    while True:
        piclink = random.randint(0, len(TELEGRAPH_MEDIA_LINKS) - 1)
        AUTOPP = TELEGRAPH_MEDIA_LINKS[piclink]
        downloaded_file_name = "./DOWNLOADS/original_pic.png"
        downloader = SmartDL(AUTOPP, downloaded_file_name, progress_bar=True)
        downloader.start(blocking=False)
        photo = "photo_pfp.png"
        while not downloader.isFinished():
            pass

        shutil.copy(downloaded_file_name, photo)
        Image.open(photo)
        current_time = datetime.now().strftime(
            "\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n                                                   Time: %H:%M:%S \n                                                   Date: %d/%m/%y "
        )
        img = Image.open(photo)
        drawn_text = ImageDraw.Draw(img)
        fnt = ImageFont.truetype(FONT_FILE_TO_USE, 30)
        drawn_text.text((300, 450), current_time, font=fnt, fill=(255, 255, 255))
        img.save(photo)
        file = await event.client.upload_file(photo)  # pylint:disable=E0602
        try:
            await event.client(
                functions.photos.UploadProfilePhotoRequest(file)  # pylint:disable=E0602
            )
            os.remove(photo)

            await asyncio.sleep(60)
        except:
            return


@legend.legend_cmd(
    pattern="indslogan(?:\s|$)([\s\S]*)",
    command=("indslogan", menu_category),
    info={
        "header": "To Get Indian Slogan",
        "usage": [
            "{tr}indslogam",
        ],
    },
)
async def _(event):
    await event.edit("Speaking A Slogan")
    await asyncio.sleep(2)
    x = random.randrange(1, 25)
    if x == 1:
        await event.edit("Inqilab Zindabad \n\n **By : Bhagat Singh**")
    if x == 2:
        await event.edit(
            "DON'T TRY TO KNOW ABUOT ME I M LEGEND✌️ @LegendBoy_XD\nfrom: @LegendBot_OP"
        )
    if x == 3:
        await event.edit("Subhash Chandra Bose : Dilli Chalo ")
    if x == 4:
        await event.edit("Mahatma Gamdhi : 'Do or die' (Karo Ya Maro)")
    if x == 5:
        await event.edit(
            "Chandra Shekhar Azad : Dushman ki goliyon ka hum samna karenge, Azad hee rahein hain, Azad hee rahenge "
        )
    if x == 6:
        await event.edit(
            "Bal Gandhar Tilak : Swaraj Mera Janamsiddh adhikar hai, aur main ise lekar rahunga"
        )
    if x == 7:
        await event.edit(
            "A.P.J Abdul Kalam : Don't take rest after your first victory because if you fail in second, more lips are waiting to say that your first victory was just luck "
        )
    if x == 8:
        await event.edit("Atal Bihari Bhajpai : Jai Jawan Jai kisan Jai Vigyan")
    if x == 9:
        await event.edit(
            "Subhash Chandra Bose : Tum Mujhe Khoon Do, main Tumhe Ajadi Doonga”. (Give me blood and I will give you freedom)"
        )
    if x == 10:
        await event.edit("Iqbal : Saare jahan se achchha hindustan hamara")
    if x == 11:
        await event.edit(
            "Ram Prasad Bismil : Sarfaroshi ki tamanna, ab hamare dil me hai"
        )
    if x == 12:
        await event.edit("Bal Gandhar Tilak : Swaraj (Self Rule) is my birthright")
    if x == 13:
        await event.edit("Rabindra Nath Tagore : Jan Gan Man Adhinayak Jaya hey")
    if x == 14:
        await event.edit(
            "Jawahar Lal Nehru : Aaram Haraam Hai (Cast off your laziness) "
        )
