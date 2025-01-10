
import logging
import asyncio
from config import Config
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = Config.ID
API_HASH = Config.HASH
SESSION1 = Config.S1
SESSION2 = Config.S2
SESSION3 = Config.S3
SESSION4 = Config.S4
SESSION5 = Config.S5
SESSION6 = Config.S6
SESSION7 = Config.S7
SESSION8 = Config.S8
SESSION9 = Config.S9
SESSION10 = Config.S10
SUDO = Config.SUDO_USERS

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

betting = None

async def main():
    global errors
    global bot1
    global bot2
    global bot3
    global bot4
    global bot5
    global bot6
    global bot7
    global bot8
    global bot9
    global bot10
    if SESSION1:
        print("Working On Bot 1!")
        try:
            bot1 = TelegramClient(
                StringSession(SESSION1),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot1.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 1 Is'nt Available")
        try:
            session_name = "session1"
            bot1 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot1.start()
        except Exception as e:
            pass
    if SESSION2:
        print("Working On Bot 2!")
        try:
            bot2 = TelegramClient(
                StringSession(SESSION2),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot2.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 2 Is'nt Available")
        try:
            session_name = "session2"
            bot2 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot2.start()
        except Exception as e:
            pass
    if SESSION3:
        print("Working On Bot 3!")
        try:
            bot3 = TelegramClient(
                StringSession(SESSION3),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot3.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 3 Is'nt Available")
        try:
            session_name = "session3"
            bot3 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot3.start()
        except Exception as e:
            pass
    if SESSION4:
        print("Working On Bot 4!")
        try:
            bot4 = TelegramClient(
                StringSession(SESSION4),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot4.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 4 Is'nt Available")
        try:
            session_name = "session4"
            bot4 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot4.start()
        except Exception as e:
            pass
    if SESSION5:
        print("Working On Bot 5!")
        try:
            bot5 = TelegramClient(
                StringSession(SESSION5),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot5.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 5 Is'nt Available")
        try:
            session_name = "session5"
            bot5 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot5.start()
        except Exception as e:
            pass
    if SESSION6:
        print("Working On Bot 1!")
        try:
            bot6 = TelegramClient(
                StringSession(SESSION6),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot6.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 6 Is'nt Available")
        try:
            session_name = "session6"
            bot6 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot6.start()
        except Exception as e:
            pass
    if SESSION7:
        print("Working On Bot 7!")
        try:
            bot7 = TelegramClient(
                StringSession(SESSION7),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot7.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 7 Is'nt Available")
        try:
            session_name = "session7"
            bot7 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot7.start()
        except Exception as e:
            pass
    if SESSION8:
        print("Working On Bot 8!")
        try:
            bot8 = TelegramClient(
                StringSession(SESSION8),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot8.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 8 Is'nt Available")
        try:
            session_name = "session8"
            bot8 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot8.start()
        except Exception as e:
            pass
    if SESSION9:
        print("Working On Bot 9!")
        try:
            bot9 = TelegramClient(
                StringSession(SESSION9),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot9.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 9 Is'nt Available")
        try:
            session_name = "session9"
            bot9 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot9.start()
        except Exception as e:
            pass
    if SESSION10:
        print("Working On Bot 10!")
        try:
            bot10 = TelegramClient(
                StringSession(SESSION10),
                api_id=API_ID,
                api_hash=API_HASH,
                )
            await bot10.start()
        except Exception as e:
            print(e)
            pass
    else:
        print("Bot 10 Is'nt Available")
        try:
            session_name = "session10"
            bot10 = TelegramClient(session_name, api_id=API_ID, api_hash=API_HASH)
            await bot10.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
