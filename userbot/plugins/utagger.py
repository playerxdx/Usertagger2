
from userbot import *

a = False

@bot1.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot2.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot3.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot4.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot5.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot6.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot7.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot8.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot9.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
@bot10.on(events.NewMessage(pattern="!utag", incoming=True, outgoing=True))
async def utag(e):
    if e.sender_id in SUDO:
        global a 
        a = True
        message = e.text[6:]
        async for users in e.client.iter_participants(e.chat_id):
            try:
                entity = await e.client.get_entity(users.id)
                get_name = entity.first_name
                get_id = entity.id
                tag = f"[{get_name}](tg://user?id={get_id})"
                if a:
                    await e.client.send_message(e.chat_id, f"{tag}\n{message}")
                    await asyncio.sleep(2.5)
            except Exception as er:
                await e.client.send_message(e.chat_id, "Something went wrong!")
                print(er)

@bot1.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot2.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot3.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot4.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot5.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot6.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot7.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot8.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot9.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
@bot10.on(events.NewMessage(pattern="!utstop", incoming=True, outgoing=True))
async def utstop(e):
    if e.sender_id in SUDO:
        global a
        a = False
        await e.client.send_message(e.chat_id, "User Tagger Stopped Successfully")
    