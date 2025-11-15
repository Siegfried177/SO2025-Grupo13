import os

"""
- rm: Elimina un archivo o carpeta
- args: <archivo>
-- No elimina carpetas ni múltiples archivos
"""
def run(args : list[str]) -> None:
    if len(args) != 1:
        print("Error: Debe haber exactamente un argumento")
        return
    
    try:
        os.remove(args[0])
    except FileNotFoundError:
        print("Error: Archivo no encontrado")
    except PermissionError:
        print("Error: Permiso denegado")
    except IsADirectoryError:
        print("Error: No se pueden eliminar directorios")