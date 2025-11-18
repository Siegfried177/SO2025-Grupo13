import os
from utils.log_gen import make_log

"""
- rm: Elimina un archivo o carpeta
- args: <archivo>
-- No elimina carpetas ni múltiples archivos
"""
def run(args : list[str]) -> None:
    if len(args) != 1:
        print("Error: Debe haber exactamente un argumento")
        make_log("rm", success=False, details="Número incorrecto de argumentos")
        return
    
    try:
        os.remove(args[0])
        make_log("rm", success=True, details=f"Archivo '{args[0]}' eliminado")
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
        make_log("rm", success=False, details="Archivo no encontrado")
    except PermissionError:
        print("Error: Permiso denegado")
        make_log("rm", success=False, details="Permiso denegado")
    except IsADirectoryError:
        print("Error: No se pueden eliminar directorios")
        make_log("rm", success=False, details="No se pueden eliminar directorios")