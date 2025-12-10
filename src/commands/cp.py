import os
from utils.log_gen import make_log
from utils.curfew_utils import is_in_curfew
from utils.lang_manager import t

"""
- cp: Copia archivos
- args: <origen> <destino + nuevo_nombre>
-- No acepta carpetas ni varios archivos
"""
def run(args : list[str]) -> None:
    if len(args) < 2: # Si no hay suficientes argumentos
        print(t("cp_missing_args"))
        make_log("cp", success=False, details="Argumentos insuficientes para el comando 'cp'")
        return
    elif len(args) > 2: # Si hay demasiados argumentos
        print(t("cp_too_many_args"))
        make_log("cp", success=False, details="Demasiados argumentos para el comando 'cp'")
        return
    
    src, dest = args[0], args[1]

    if os.path.exists(dest) and is_in_curfew():
        print(t("cp_restricted"))
        make_log("cp", success=False, details="Comando restringido para sobreescribir durante el toque de queda") 
        return

    # Si dest es un directorio existente, agregar el nombre del archivo
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))
    
    try:
        with open(src, "rb") as f_src: # Abrir el archivo de origen en modo lectura binaria "rb"
            with open(dest, "wb") as f_dst: # Abrir/crear archivo destino
                while True:
                    chunk = f_src.read(4096)
                    if not chunk:
                        break
                    f_dst.write(chunk)
        make_log(f"cp {src} {dest}", success=True, details=f"Archivo copiado exitosamente")
    except FileNotFoundError:
        print(t("cp_file_not_found").format(src))
        make_log(f"cp {src} {dest}", success=False, details=f"El archivo no existe")
        return
    except PermissionError:
        print(t("cp_no_permission"))
        make_log(f"cp {src} {dest}", success=False, details="No tiene permiso")
        return
