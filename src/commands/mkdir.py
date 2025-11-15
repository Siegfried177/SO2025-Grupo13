import os

"""
- mkdir: Crea un nuevo directorio
- args: [dirección + nombre] o [nombre]
-- No puede crear un directorio si ya existe, ni crear múltples directorios a la vez, no está implementado '-p'
"""
def run(args : list[str]) -> None:
    if len(args) > 1:
        print("Error: Demasiados argumentos para 'mkdir'")
        return
    
    if len(args) == 0:
        print("Error: Se requiere un nombre de directorio para 'mkdir'")
        return
    
    dir_name = args[0] if len(args) == 1 else args[1]
    if len(args) == 1:
        dir_path = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print(f"Error: El directorio '{dir_name}' ya existe")
        except PermissionError:
            print(f"Error: No tienes permiso para crear el directorio '{dir_name}'")