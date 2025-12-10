import os
from datetime import datetime
from .var import current_user
from utils.lang_manager import t
from utils import var

# Constantes para los directorios y archivos de log
SUCCESS_LOG = os.path.join(var.SHELL_DIR, "shell.log")
ERROR_LOG = os.path.join(var.SHELL_DIR, "sistema_error.log")

# Crear directorio de logs si no existe
if not os.path.exists(var.SHELL_DIR):
    try:
        os.makedirs(var.SHELL_DIR)
    except PermissionError:
        print(t("log_cannot_create_dir"))  # ← reemplazo
        

# Función para realizar el logging de acciones y errores
def make_log(command, success=True, details=""):
    timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    log_file = SUCCESS_LOG if success else ERROR_LOG # Se decide si es un log de acción exitosa o de error
    
    if success:
        log_line = f"[{timestamp}] {current_user} -- {command} -- EXITO -- {details}\n"
    else:
        log_line = f"[{timestamp}] {current_user} -- {command} -- FRACASO -- {details}\n"

    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(log_line)
    except Exception as e:
        print(t("log_cannot_write"))  # ← reemplazo
