import os
from utils.log_gen import make_log
from utils.lang_manager import t

"""
- rm: Elimina un archivo o carpeta
- args: <archivo>
-- No elimina carpetas ni múltiples archivos
"""
def run(args : list[str]) -> None:
    if len(args) != 1:
        print(t("rm_one_arg"))
        make_log("rm", success=False, details="Número incorrecto de argumentos")
        return
    
    try:
        os.remove(args[0])
        make_log("rm", success=True, details=f"Archivo '{args[0]}' eliminado")
    except FileNotFoundError:
        print(t("rm_not_found"))
        make_log("rm", success=False, details="Archivo no encontrado")
    except PermissionError:
        print(t("rm_no_permission"))
        make_log("rm", success=False, details="Permiso denegado")
    except IsADirectoryError:
        print(t("rm_is_directory"))
        make_log("rm", success=False, details="No se pueden eliminar directorios")