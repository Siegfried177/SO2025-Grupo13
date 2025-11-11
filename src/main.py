import os, importlib, pkgutil, commands
from utils.parser import parse_command

lang : str = "es"
commands_dict : dict[str, object] = {}
current_user : str = "cyaluk"

for loader, module_name, is_pkg in pkgutil.iter_modules(commands.__path__):
    module : object = importlib.import_module(f"commands.{module_name}")
    commands_dict[module_name] = module.run

while True:
    cmd_input = input(f"${current_user} ")
    cmd_parsed = parse_command(cmd_input)
    
    if not cmd_parsed: continue
    
    cmd_name = cmd_parsed[0]
    cmd_args = cmd_parsed[1:]
    
    if cmd_name in commands_dict:
        commands_dict[cmd_name](cmd_args)
    else: print(f"No existe el comando '{cmd_name}'")