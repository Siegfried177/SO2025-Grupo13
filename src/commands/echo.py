from utils.log_gen import make_log
from utils.lang_manager import t

"""
- echo: Imprime texto en la consola
- args: [texto] no importan los espacios
        [texto] [>] [archivo]
        [texto] [>>] [archivo]
-- [>] Redirige la salida a un archivo en lugar de imprimir en consola, si ya existe el archivo se sobrescribe
-- [>>] Redirige la salida a un archivo en lugar de imprimir en consola, si ya existe se añade al final del archivo
"""
def run(args : list[str]) -> None:
    if len(args) == 0:
        print()
        make_log("echo")
        return
    
    if len(args) == 1 : # Si no hay redirección, imprimir en consola
        print(args[0])
        make_log("echo")
        return
    
    if ">" == args[1]: # Si hay redirección de salida a un archivo (sobrescribir)
        index : int = args.index(">")
        text : str = " ".join(args[:index])
        
        if index + 1 >= len(args): # Si no se especificó el archivo
            print(t("echo_no_file"))
            make_log("echo", success=False, details="No se especificó el archivo para redirigir la salida")
            return
        new_file_name : str = args[index + 1]

        try:
            with open(new_file_name, "w", encoding="utf-8") as f:
                f.write(text)
                make_log("echo", success=True, details=f"Salida redirigida a '{new_file_name}' -- Sobrescribir")
        except Exception as e:
            print(t("echo_write_error").format(new_file_name))
            make_log("echo", success=False, details=f"Error al escribir en el archivo '{new_file_name}'")
    
    elif ">>" in args: # Si hay redirección de salida a un archivo (añadir al final)
        index : int = args.index(">>")
        text : str = " ".join(args[:index])
        new_file_name : str = args[index + 1]
        
        if index + 1 >= len(args): # Si no se especificó el archivo
            print(t("echo_no_file"))
            make_log("echo", success=False, details="No se especificó el archivo para redirigir la salida")
            return

        try:
            with open(new_file_name, "a", encoding="utf-8") as f:
                f.write(text)
                make_log("echo", success=True, details=f"Salida redirigida a '{new_file_name}' -- Añadir al final")
        except Exception as e:
            print(t("echo_write_error").format(new_file_name))
            make_log("echo", success=False, details=f"Error al escribir en el archivo '{new_file_name}'")
