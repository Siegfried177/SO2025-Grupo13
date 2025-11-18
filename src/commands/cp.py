import os
from utils.log_gen import make_log

"""
- cp: Copia archivos
- args: <origen> <destino + nuevo_nombre>
-- No acepta carpetas ni varios archivos
"""
def run(args : list[str]) -> None:
    if len(args) < 2: # Si no hay suficientes argumentos
        print("Error: Se debe indicar el archivo de origen y el destino")
        make_log("cp", success=False, details="Argumentos insuficientes para el comando 'cp'")
        return
    elif len(args) > 2: # Si hay demasiados argumentos
        print("Error: Demasiados argumentos para el comando 'cp'")
        make_log("cp", success=False, details="Demasiados argumentos para el comando 'cp'")
        return
    
    src, dest = args[0], args[1]

    # Si dest es un directorio existente, agregar el nombre del archivo
    if os.path.isdir(dest):
        dest = os.path.join(dest, os.path.basename(src))
    
    try:
        with open(src, "rb") as f_src: # Abrir el archivo de origen en modo lectura binaria "rb" (debe ser binario para copiar cualquier tipo de archivo)
            with open(dest, "wb") as f_dst: # Abrir/crear el archivo de destino en modo escritura binaria "wb"
                while True:
                    chunk = f_src.read(4096) # Leer el archivo de origen en bloques de 4096 bytes (Suele ser el tamaño comun)
                    if not chunk:
                        break
                    f_dst.write(chunk)
        make_log(f"cp {src} {dest}", success=True, details=f"Archivo copiado exitosamente")
    except FileNotFoundError:
        print(f"Error: El archivo '{src}' no existe")
        make_log(f"cp {src} {dest}", success=False, details=f"El archivo no existe")
        return
    except PermissionError:
        print(f"Error: No tiene permiso")
        make_log(f"cp {src} {dest}", success=False, details="No tiene permiso")
        return