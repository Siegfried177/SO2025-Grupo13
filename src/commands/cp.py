
"""
- cp: Copia archivos
- args: <origen> <destino + nuevo_nombre>
-- No acepta carpetas ni varios archivos
"""
def run(args : list[str]) -> None:
    if len(args) < 2: # Si no hay suficientes argumentos
        print("Error: Se debe indicar el archivo de origen y el destino")
        return
    elif len(args) > 2: # Si hay demasiados argumentos
        print("Error: Demasiados argumentos para el comando 'cp'")
        return
    
    src, dest = args[0], args[1]
    
    try:
        with open(src, "rb") as f_src: # Abrir el archivo de origen en modo lectura binaria "rb" (debe ser binario para copiar cualquier tipo de archivo)
            with open(dest, "wb") as f_dst: # Abrir/crear el archivo de destino en modo escritura binaria "wb"
                while True:
                    chunk = f_src.read(4096) # Leer el archivo de origen en bloques de 4096 bytes (Suele ser el tamaño comun)
                    if not chunk:
                        break
                    f_dst.write(chunk)
    except FileNotFoundError:
        print(f"Error: El archivo '{src}' no existe")
    except PermissionError:
        print(f"Error: No se pueden copiar directorios")