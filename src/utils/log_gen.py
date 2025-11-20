import os
from datetime import datetime
from .var import current_user

# Constantes para los directorios y archivos de log
LOG_DIR = "C:\\aaaaaaaa"
ACTION_LOG = os.path.join(LOG_DIR, "shell.txt")
ERROR_LOG = os.path.join(LOG_DIR, "sistema_error.txt")

# Crear directorio de logs si no existe
if not os.path.exists(LOG_DIR):
    try:
        os.makedirs(LOG_DIR)
    except PermissionError:
        print("Error: No se pudo crear el directorio de logs. Ejecuta como administrador/root.")

# Función para realizar el logging de acciones y errores
def make_log(command, success=True, details=""):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log_file = ACTION_LOG if success else ERROR_LOG # Se decide si es un log de acción exitosa o de error
    
    if success:
        log_line = f"[{timestamp}] {current_user} -- {command} -- EXITO -- {details}\n"
    else:
        log_line = f"[{timestamp}] {current_user} -- {command} -- FRACASO -- {details}\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print(f"Error: No se pudo escribir el log: {e}")