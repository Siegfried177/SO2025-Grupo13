
"""
- parse_command: Parsea la entrada del usuario en una lista de comandos y argumentos
- input_str: String input del usuario
- return: Lista de strings con el comando y sus argumentos
"""
def parse_command(input_str : str) -> list[str]:
    return input_str.strip().split()