import importlib, pkgutil, commands
from utils import curfew_utils, lang_manager, var, parser, log_gen
from utils.lang_manager import t

# Iterar sobre todos los módulos en el paquete commands, añadir cada comando al diccionario con su función lista para ejecutarse
for loader, module_name, is_pkg in pkgutil.iter_modules(commands.__path__): 
    module : object = importlib.import_module(f"commands.{module_name}")
    var.commands_dict[module_name] = module.run

log_gen.make_log("Shell iniciada") # Registrar el inicio de la shell
curfew_utils.load_curfew() # Cargar el toque de queda
var.set_user() # Establecer el usuario actual
lang_manager.load_lang() # Cargar el idioma

while True:
    cmd_input = input(f"{var.current_user} {var.current_dir}> $ ")
    cmd_parsed = parser.parse_command(cmd_input)
    
    if not cmd_parsed: continue # Si no se escribió nada, continuar el loop
    
    cmd_name = cmd_parsed[0]
    cmd_args = cmd_parsed[1:]
    
    if cmd_name in var.commands_dict: # Si el comando es correcto
        if curfew_utils.is_in_curfew() and cmd_name in var.restricted_commands: # Si el toque de queda está activo y el comando está restringido
            print(t("shell_cmd_restricted").format(cmd_name))
            log_gen.make_log(cmd_name, success=False, details="Comando restringido durante el toque de queda")
            continue
        
        if var.input_limit != 0 and len(cmd_input) > var.input_limit: # Si el comando excede el límite de caracteres permitidos (0 = sin limite)
            print(t("shell_input_limit").format(var.input_limit))
            log_gen.make_log(cmd_name, success=False, details="Límite de caracteres excedido")
            continue

        var.commands_dict[cmd_name](cmd_args)
    else: 
        print(t("shell_cmd_not_found").format(cmd_name))
        log_gen.make_log(cmd_name, success=False, details="No existe el comando indicado")
