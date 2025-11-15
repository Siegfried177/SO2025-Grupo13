
"""
- echo: Imprime texto en la consola
- args: [texto]
        [texto] [>] [archivo]
-- [>] Redirige la salida a un archivo en lugar de imprimir en consola, si ya existe el archivo se sobrescribe
"""
def run(args : list[str]) -> None:
    if len(args) == 0:
        print()
        return
    
    if ">" in args: # Si hay redirección de salida a un archivo
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
    
    else: # Si no hay redirección, imprimir en consola
        print(" ".join(args))