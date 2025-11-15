import os

"""
- set_current_dir: Actualiza el directorio actual y previo
- path: Nuevo directorio
"""
def set_current_dir(path : str) -> None:
    global previous_dir, current_dir 
    previous_dir = current_dir
    current_dir = path

lang : str = "es" # Idioma de la shell
commands_dict : dict[str, object] = {} # Diccionario de comandos disponibles
current_user : str = "cyaluk" # Usuario actual
previous_dir : str = os.getcwd() # Directorio previo
current_dir : str = os.getcwd() # Directorio actual