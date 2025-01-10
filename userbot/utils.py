
import sys
import logging
import importlib
from pathlib import Path

def load_plugs(plugname):
    modules = Path(f"userbot/plugins/{plugname}.py")
    myfiles = f"userbot.plugins.{plugname}"
    spec = importlib.util.spec_from_file_location(myfiles, modules)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugname)
    spec.loader.exec_module(load)
    sys.modules["userbot.plugins." + plugname] = load
    print("Userbot - Successfully Imported " + plugname)
    