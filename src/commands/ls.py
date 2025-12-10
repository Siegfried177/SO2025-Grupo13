import os 
from utils.log_gen import make_log
from utils.lang_manager import t

"""
- ls: Lista archivos y directorios
- args: [-a] [directorio]
        [directorio]
-- Si no hay argumentos lista el directorio actual
-- Muestra archivos ocultos si se usa -a
"""
def run(args : list[str]) -> None:
    if len(args) > 2:  # Demasiados argumentos
        print(t("ls_too_many_args"))
        make_log("ls", success=False, details="Demasiados argumentos para 'ls'")
        return
    
    if len(args) == 0:
        list_dir : list = os.listdir()
        list_dir = [item for item in list_dir if not item.startswith('.')]
        for item in list_dir:
            print(item)
        make_log("ls")
        return
    
    hidden_items : bool = True if args[0] == "-a" else False
    
    if len(args) == 2:
        if hidden_items:
            list_dir : list = os.listdir(args[1])
            try:
                for item in list_dir:
                    print(item)
                make_log("ls")
            except FileNotFoundError:
                print(t("ls_dir_not_found").format(args[1]))
                make_log("ls", success=False, details=f"No existe el directorio '{args[1]}'")
                return
        else:
            print(t("ls_invalid_args"))
            make_log("ls", success=False, details="Argumento/s no reconocido/s para 'ls'")
            return
    
    elif len(args) == 1:
        if hidden_items:
            list_dir : list = os.listdir()
            try:
                for item in list_dir:
                    print(item)
                make_log("ls")
            except FileNotFoundError:
                print(t("ls_dir_not_found").format(args[0]))
                make_log("ls", success=False, details=f" No existe el directorio '{args[0]}'")
        else:
            list_dir = os.listdir(args[0])
            list_dir = [item for item in list_dir if not item.startswith('.')]
            try:
                for item in list_dir:
                    print(item)
                make_log("ls")
            except FileNotFoundError:
                print(t("ls_dir_not_found").format(args[0]))
                make_log("ls", success=False, details=f"No existe el directorio '{args[0]}'")
                return