import os
from utils.log_gen import make_log

"""
- pwd: Muestra el directorio actual
- args: Ninguno
"""
def run(args : list[str]) -> None:
    if len(args) > 0:  # Si se pasan argumentos
        print("Error: El comando 'pwd' no acepta argumentos")
        make_log("pwd", success=False, details="El comando 'pwd' no acepta argumentos")
        return
    
    current_dir = os.getcwd()
    print(current_dir)
    make_log("pwd")