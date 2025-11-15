import os
from utils import var

"""
- cd: Cambia el directorio actual
- args: [directorio]
        [~] o [..] o [-]
-- Si no hay argumentos o [~] cambia al directorio Home
-- [..] Cambia al directorio padre
-- [-] Cambia al directorio anterior
"""
def run(args : list[str]) -> None:
    if len(args) > 1:  # Demasiados argumentos
        print("Error: Demasiados argumentos para 'cd'")
        return
    
    if len(args) == 0 or args[0] == "~": # Cambiar al directorio Home
        os.chdir(os.path.expanduser("~"))
        var.set_current_dir(os.getcwd())
        return
    
    if args[0] == "-": # Cambiar al directorio anterior
        os.chdir(var.previous_dir)
        var.set_current_dir(os.getcwd())
        return
    
    if args[0] == "..": # Cambiar al directorio padre
        os.chdir(os.path.dirname(var.current_dir))
        var.set_current_dir(os.getcwd())
        return
    
    try:
        os.chdir(os.path.expanduser(args[0]))
    except FileNotFoundError:
        print(f"Error: El directorio '{args[0]}' no existe")
    except PermissionError:
        print(f"Error: No tienes permiso para acceder al directorio '{args[0]}'")
    
    var.set_current_dir(os.getcwd())