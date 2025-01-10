
import glob
from pathlib import Path
from sys import argv
from userbot import *
from userbot.utils import load_plugs

if __name__ == "__main__":
    modules = "userbot/plugins/*.py"
    plugins = glob.glob(modules)
    for myfiles in plugins:
        with open(myfiles) as f:
            module = Path(f.name)
            plugname = module.stem
            load_plugs(plugname.replace(".py", ""))

print("\n\nUserbot Deployed Successfully!\n\n")

if len(argv) not in (1, 3, 4):
    try:
        bot1.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot2.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot3.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot4.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot5.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot6.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot7.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot8.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot9.disconnect()
    except Exception as e:
        print(e)
        pass
    try:
        bot10.disconnect()
    except Exception as e:
        print(e)
        pass
else:
    try:
        bot1.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot2.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot3.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot4.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot5.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot6.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot7.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot8.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot9.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
    try:
        bot10.run_until_disconnected()
    except Exception as e:
        print(e)
        pass
