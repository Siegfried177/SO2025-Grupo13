import sys

"""
- exit: Termina la ejecución de la Shell
- args: Ninguno
"""
def run(args : list[str]) -> None:
    if len(args) > 0:  # Si se pasan argumentos
        print("Error: El comando 'exit' no acepta argumentos")
        return
    
    sys.exit()