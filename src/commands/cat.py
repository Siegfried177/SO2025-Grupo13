
"""
- cat: Muestra el contenido de un archivo
- args: [archivo]
-- El encoding debe ser UTF-8
"""
def run(args : list[str]) -> None:
	if len(args) != 1:
		print("Error: Debe haber exactamente un argumento")
		return
	
	try:
		with open(args[0], "r", encoding="utf-8") as f:
			print(f.read())
	except FileNotFoundError:
		print(f"Error: El archivo '{args[0]}' no existe")
	except PermissionError:
		print(f"Error: No tienes permiso para leer el archivo '{args[0]}'")