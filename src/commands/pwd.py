import os

"""
- pwd: Muestra el directorio actual
- args: Ninguno
"""
def run(args : list[str]) -> None:
    if len(args) > 0:  # Si se pasan argumentos
        print("Error: El comando 'pwd' no acepta argumentos")
        return
    
    current_dir = os.getcwd()
    print(current_dir)