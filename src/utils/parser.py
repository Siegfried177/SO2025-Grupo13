
"""
- parse_command: Parsea la entrada del usuario en una lista de comandos y argumentos
- input_str: String input del usuario
- return: Lista de strings con el comando y sus argumentos
-- Soporta argumentos entre comillas dobles para permitir espacios dentro de un solo argumento
"""
def parse_command(input_str : str) -> list[str]:
    if '"' in input_str:  # Manejar argumentos entre comillas dobles para que sirvan como uno solo
        args = []
        current_part = ""
        in_quotes = False
        
        for char in input_str:
            if char == '"': # Alternar el estado de comillas
                in_quotes = not in_quotes
                if not in_quotes:
                    args.append(current_part)
                    current_part = ""
            elif char == ' ' and not in_quotes: # Separar por espacios solo si no está entre comillas
                if current_part:
                    args.append(current_part)
                    current_part = ""
            else: # Agregar el caracter al argumento actual
                current_part += char
        
        if current_part: # Agregar el ultimo argumento si existe
            args.append(current_part)
        
        return args
    
    return input_str.strip().split() # Separar por espacios normales si no hay comillas