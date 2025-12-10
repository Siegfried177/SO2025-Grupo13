import os, getpass, platform
from pathlib import Path

if platform.system() == "Linux":
    SHELL_DIR = Path.home() / ".shell_data"
else:
    SHELL_DIR = Path("C:\\Shell")

"""
- set_current_dir: Actualiza el directorio actual y el anterior
- path: Nuevo directorio
"""
def set_current_dir(path : str) -> None:
    global previous_dir, current_dir 
    
    previous_dir = current_dir
    current_dir = path

"""
- set_user: Coloca el usuario actual en la variable current_user
"""
def set_user() -> None:
    global current_user
    current_user = getpass.getuser()

lang : str = "es" # Idioma de la shell
commands_dict : dict[str, object] = {} # Diccionario de comandos disponibles
current_user : str = "cyaluk" # Usuario actual
previous_dir : str = os.getcwd() # Directorio anterior
current_dir : str = os.getcwd() # Directorio actual

### VARIABLES DEL TOQUE DE QUEDA (curf) ###
curfew_on: bool = True # Estado del toque de queda
curfew_period: list[str] = ["22:00", "06:00"] # Horas del toque de queda
restricted_commands : list[str] = ["rm"]# Comandos restringidos durante el toque de queda

### VARIABLES DEL LIMITE DE CARACTERES (inputlimit) ###
input_limit : int = 0 # Límite de caracteres para los comandos (0 = sin límite)