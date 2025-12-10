import sys
from utils.log_gen import make_log
from utils.lang_manager import t

"""
- exit: Termina la ejecución de la Shell
- args: Ninguno
"""
def run(args : list[str]) -> None:
    if len(args) > 0:  # Si se pasan argumentos
        print(t("exit_no_args"))
        make_log("exit", success=False, details="El comando 'exit' no acepta argumentos")
        return
    
    make_log("exit")
    sys.exit(0)
