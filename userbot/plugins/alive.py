
from userbot import *

@bot1.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot2.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot3.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot4.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot5.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot6.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot7.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot8.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot9.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
@bot10.on(events.NewMessage(pattern="!alive", incoming=True, outgoing=True))
async def alive(e):
    if e.sender_id in SUDO:
        await e.client.send_message(e.chat_id, "𝐔𝐬𝐞𝐫𝐛𝐨𝐭 𝐈𝐬 𝐀𝐥𝐢𝐯𝐞!")
