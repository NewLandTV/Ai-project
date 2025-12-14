import os
from importlib import import_module

prefix = "/run "
directory = os.path.dirname(__file__)

def try_run(command):
    if not command.startswith(prefix):
        return False
    
    length = len(prefix)
    command = command[length:]
    split = command.split(".")
    path = os.path.join(*split)
    if len(command) == 0 or not os.path.exists(os.path.join(directory, path)):
        return False
    
    module = import_module(f"commands.{command}")
    module.run()

    return True