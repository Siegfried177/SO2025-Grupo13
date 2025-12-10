import os
from utils.log_gen import make_log
from utils.lang_manager import t

"""
- mkdir: Crea un nuevo directorio
- args: [dirección + nombre] o [nombre]
-- No puede crear un directorio si ya existe, ni crear múltples directorios a la vez, no está implementado '-p'
"""
def run(args : list[str]) -> None:
    if len(args) > 1:
        print(t("mkdir_too_many_args"))
        make_log("mkdir", success=False, details="Demasiados argumentos para 'mkdir'")
        return
    
    if len(args) == 0:
        print(t("mkdir_missing_name"))
        make_log("mkdir", success=False, details="Se requiere un nombre de directorio para 'mkdir'")
        return
    
    dir_name = args[0] if len(args) == 1 else args[1]
    if len(args) == 1:
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_path)
            make_log("mkdir", success=True, details=f"Directorio '{dir_path}' creado")
        except FileExistsError:
            print(t("mkdir_exists").format(dir_name))
            make_log("mkdir", success=False, details=f"El directorio '{dir_name}' ya existe")
        except PermissionError:
            print(t("mkdir_no_permission").format(dir_name))
            make_log("mkdir", success=False, details=f"No tienes permiso para crear el directorio '{dir_name}'")
