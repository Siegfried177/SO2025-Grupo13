from utils.log_gen import make_log
from utils.lang_manager import t

"""
- cat: Muestra el contenido de un archivo
- args: [archivo]
-- El encoding debe ser UTF-8
"""
def run(args : list[str]) -> None:
	if len(args) != 1:
		print(t("cat_one_arg"))
		make_log("cat", success=False, details="Debe haber exactamente un argumento")
		return
	
	try:
		with open(args[0], "r", encoding="utf-8") as f:
			print(f.read())
		make_log(f"cat {args[0]}")
	except FileNotFoundError:
		print(t("cat_file_not_found").format(args[0]))
		make_log(f"cat {args[0]}", success=False, details=f"El archivo '{args[0]}' no existe")
	except PermissionError:
		print(t("cat_no_permission").format(args[0]))
		make_log(f"cat {args[0]}", success=False, details=f"No tienes permiso para leer el archivo '{args[0]}'")
