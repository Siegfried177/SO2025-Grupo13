
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
        return
    
    if ">" == args[1]: # Si hay redirección de salida a un archivo (sobrescribir)
        index = args.index(">")
        text = " ".join(args[:index])
        
        if index + 1 >= len(args): # Si no se especificó el archivo
            print("Error: No se especificó el archivo para redirigir la salida")
            return
        new_file_name = args[index + 1]

        try:
            with open(new_file_name, "w", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print(f"Error: Error al escribir en el archivo '{new_file_name}'")
    
    elif ">>" in args: # Si hay redirección de salida a un archivo (añadir al final)
        index = args.index(">>")
        text = " ".join(args[:index])
        new_file_name = args[index + 1]
        
        if index + 1 >= len(args): # Si no se especificó el archivo
            print("Error: No se especificó el archivo para redirigir la salida")
            return

        try:
            with open(new_file_name, "a", encoding="utf-8") as f:
                f.write(text)
        except Exception as e:
            print(f"Error: Error al escribir en el archivo '{new_file_name}'")
    
    else: # Si no hay redirección, imprimir en consola
        print(" ".join(args))