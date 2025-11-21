import os

"""
- set_current_dir: Actualiza el directorio actual y el anterior
- path: Nuevo directorio
"""
def set_current_dir(path : str) -> None:
    global previous_dir, current_dir 
    
    previous_dir = current_dir
    current_dir = path

lang : str = "es" # Idioma de la shell
commands_dict : dict[str, object] = {} # Diccionario de comandos disponibles
current_user : str = "cyaluk" # Usuario actual
SHELL_DIR: str = "C:\\Shell"
previous_dir : str = os.getcwd() # Directorio anterior
current_dir : str = os.getcwd() # Directorio actual

curfew_on: bool = True # Estado del toque de queda
curfew_period: list[str] = ["22:00", "06:00"] # Horas del toque de queda
restricted_commands : list[str] = ["rm"]# Comandos restringidos durante el toque de queda