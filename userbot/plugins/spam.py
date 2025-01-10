
from userbot import *

a = False

@bot1.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot2.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot3.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot4.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot5.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot6.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot7.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot8.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot9.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
@bot10.on(events.NewMessage(pattern="!uspam", incoming=True, outgoing=True))
async def uspam(e):
    if e.sender_id in SUDO:
        global a
        a = True
        if e.is_reply == True:
            replied = await e.get_reply_message()
            replied_message = replied.message
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, replied_message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        else:
            message = e.text[6:]
            try:
                while a == True:
                    await e.client.send_message(e.chat_id, message)
            except Exception as er:
                print(er)
                await e.client.send_message(e.chat_id, "Something Went Wrong! Reply to a message or type a message to spam!")
        
@bot1.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot2.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot3.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot4.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot5.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot6.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot7.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot8.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot9.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
@bot10.on(events.NewMessage(pattern="!ustop", incoming=True, outgoing=True))
async def ustop(e):
    if e.sender_id in SUDO:
        global a
        a = False
        await e.client.send_message(e.chat_id, "U Spam Stopped Successfully")
