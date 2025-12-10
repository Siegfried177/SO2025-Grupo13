from utils import lang_manager, var
from utils.log_gen import make_log
from utils.lang_manager import t

"""
- chlan: Cambia el idioma de la shell (Español o Inglés)
- args: ["es" / "en"]
        [--help]
-- Solo afecta a los prints, los logs siempre estarán en español
-- --help muestra la ayuda del comando
"""
def run(args : list[str]) -> None:
    if len(args) == 1 and args[0] == "--help": # Mostrar ayuda del comando
        print(t("chlan_help_usage"))
        print(t("chlan_help_desc"))
        print(t("chlan_help_note"))
        return
    
    if len(args) != 1 or args[0] not in ["es", "en"]:
        print(t("chlan_invalid_arg"))
        make_log("chlan", success=False, details="Argumento inválido")
        return
    
    if (args[0] == var.lang): # Si el idioma ya estaba establecido, no se cambia
        print(t("chlan_already_set"))
        make_log("chlan", details="Ese ya es el idioma establecido")
        return
    
    lang_manager.set_lang(args[0])
    print(t("chlan_changed_es") if args[0] == "es" else t("chlan_changed_en"))
    make_log("chlan", details=f"Idioma cambiado a {'Español' if args[0] == 'es' else 'Inglés'}")
