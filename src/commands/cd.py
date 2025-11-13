import os
from utils import var

def run(args):
    if len(args) > 1:  # Demasiados argumentos
        print("Demasiados argumentos para 'cd'")
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
        print(f"El directorio '{args[0]}' no existe")
    except PermissionError:
        print(f"No tienes permiso para acceder al directorio '{args[0]}'")
    
    var.set_current_dir(os.getcwd())