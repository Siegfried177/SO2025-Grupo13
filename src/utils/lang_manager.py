from utils import var
from utils.lang import es, en
from utils.var import SHELL_DIR

LANG_TABLE = {
    "es": es.OUTPUT_TEXT,
    "en": en.OUTPUT_TEXT
}

'''
- load_lang: Establece el idioma de la shell según el archivo lang.txt
'''
def load_lang() -> None:
    try: 
        with open(f"{SHELL_DIR}\\lang.txt", "r") as f: # Se abre el archivo para saber el estado del toque de queda (on / off)
            lang = f.readline().strip() # Se lee el texto del archivo
            print(lang)
        if lang in ["es", "en"]:
            var.lang = lang
        else:
            var.lang = "es"  # Idioma español por defecto
            with open(f"{SHELL_DIR}\\lang.txt", "w") as f: # Se sobreescribe el archivo con el idioma por defecto
                f.write("es\n")  # Idioma español por defecto
    except FileNotFoundError:
        print(t("lang_file_missing"))
        var.lang = "es"  # Idioma español por defecto
        
        with open(f"{SHELL_DIR}\\lang.txt", "w") as f: # Se crea el archivo con el idioma por defecto
            f.write("es\n")  # Idioma español por defecto

'''
- set_lang: Establece el idioma de la shell y guarda la configuración en lang.txt
- lang: Idioma ("es" / "en")
'''
def set_lang(lang : str) -> None:
    var.lang = lang
    try:
        with open(f"{SHELL_DIR}\\lang.txt", "w") as f:
            f.write(lang + "\n")
    except Exception as e:
        print(t("lang_save_error"))
    try: 
        with open(f"{SHELL_DIR}\\lang.txt", "w") as f: 
            f.write(lang + "\n")
    except FileNotFoundError:
        print(t("lang_file_missing"))
        
        with open(f"{SHELL_DIR}\\lang.txt", "w") as f: # Se crea el archivo con el idioma por defecto
            f.write("es\n")  # Idioma español por defecto

'''
- t: Traduce una clave de texto según el idioma actual
- key: Clave de texto a traducir
- return: Texto traducido
'''
def t(key : str) -> str:
    table = LANG_TABLE[var.lang]
    return table[key]