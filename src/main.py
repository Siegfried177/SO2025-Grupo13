import importlib, pkgutil, commands
from utils import var, parser

# Iterar sobre todos los módulos en el paquete commands, añadir cada comando al diccionario con su función lista para ejecutarse
for loader, module_name, is_pkg in pkgutil.iter_modules(commands.__path__): 
    module : object = importlib.import_module(f"commands.{module_name}")
    var.commands_dict[module_name] = module.run

while True:
    cmd_input = input(f"{var.current_user} {var.current_dir}> $ ")
    cmd_parsed = parser.parse_command(cmd_input)
    
    if not cmd_parsed: continue # Si no se escribió nada, continuar el loop
    
    cmd_name = cmd_parsed[0]
    cmd_args = cmd_parsed[1:]
    
    if cmd_name in var.commands_dict:
        var.commands_dict[cmd_name](cmd_args)
    else: print(f"No existe el comando '{cmd_name}'")