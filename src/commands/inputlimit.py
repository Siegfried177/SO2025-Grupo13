from utils.log_gen import make_log
from utils.curfew_utils import is_in_curfew
from utils import var
from utils.lang_manager import t

"""
- inputlimit: Establece un límite de caracteres para los comandos
- args: [número]
        [--help]
-- El número debe ser entero positivo o 0
-- 0 = sin límite
-- --help muestra la ayuda del comando
"""
def run(args : list[str]) -> None:
    if len(args) == 0:
        print(t("inputlimit_missing_arg"))
        make_log("inputlimit", success=False, details="Faltan argumentos")
        return
    
    if args[0] == "--help": # Mostrar ayuda del comando
        print(t("inputlimit_help_usage"))
        print(t("inputlimit_help_desc"))
        print(t("inputlimit_help_rules"))
        return
    
    if (len(args) != 1) or (not args[0].isdigit()) or (int(args[0]) < 0): # Validar argumento
        print(t("inputlimit_invalid_arg"))
        make_log("inputlimit", success=False, details="Argumento inválido")
        return
    
    var.input_limit = int(args[0])
    print(t("inputlimit_set").format(var.input_limit))
    make_log("inputlimit", details=f"Límite de caracteres establecido a {var.input_limit}")
