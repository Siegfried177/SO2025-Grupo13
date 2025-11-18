import sys
from utils.log_gen import make_log

"""
- exit: Termina la ejecución de la Shell
- args: Ninguno
"""
def run(args : list[str]) -> None:
    if len(args) > 0:  # Si se pasan argumentos
        print("Error: El comando 'exit' no acepta argumentos")
        make_log("exit", success=False, details="El comando 'exit' no acepta argumentos")
        return
    
    make_log("exit")
    sys.exit(0)