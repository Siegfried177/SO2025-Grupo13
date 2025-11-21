from utils.var import restricted_commands, SHELL_DIR
from utils.log_gen import make_log

# load_restricted_commands: Carga la lista de comandos restringidos desde el archivo "restricted_cmds.log"
def load_restricted_commands() -> None:
    global restricted_commands
    
    try:
        with open(f"{SHELL_DIR}\\restricted_cmds.log", "r") as f: # Se abre el archivo y se lee la lista de comandos restringidos
            restricted_commands = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print("Error: El archivo 'restricted_cmds.log' no existe, se creará uno con los comandos por defecto 'rm' y 'cp'")
        make_log("curf", success=False, details="El archivo 'restricted_cmds.log' no existe, se creará uno con los comandos por defecto")
        restricted_commands = ["rm"]  # Comando restringido por defecto, cp no está por que solo está restringido en parte
        
        with open(f"{SHELL_DIR}\\restricted_cmds.log", "w") as f: # Se crea el archivo con los comandos por defecto
            for cmd in restricted_commands:
                f.write(cmd + "\n")

'''
- save_restricted_commands: Guarda la lista de comandos restringidos en el archivo "restricted_cmds.log"
'''
def save_restricted_commands() -> None:
    global restricted_commands
    
    try:
        with open("restricted_cmds.log", "w") as f:
            for cmd in restricted_commands:
                f.write(cmd + "\n")
    except Exception as e:
        print(f"Error al guardar la lista de comandos restringidos: {e}")
        make_log("curf", success=False, details=f"Error al guardar la lista de comandos restringidos: {e}")

'''
- load_curfew_period: Carga el periodo de toque de queda desde el archivo "curfew_period.log"
'''
def load_curfew_period() -> None:
    global curfew_period
    
    try:
        with open("curfew_period.log", "r") as f:
            lines = [line.strip() for line in f if line.strip()]
            if len(lines) >= 2:
                curfew_period = [lines[0], lines[1]]
    except FileNotFoundError:
        print("Error: El archivo 'curfew_period.log' no existe, se creará uno con el periodo por defecto '22:00 - 06:00'")
        make_log("curf", success=False, details="El archivo 'curfew_period.log' no existe, se creará uno con el periodo por defecto")
        curfew_period = ["22:00", "06:00"]  # Periodo por defecto
        
        with open("curfew_period.log", "w") as f:
            f.write(f"{curfew_period[0]}\n")
            f.write(f"{curfew_period[1]}\n")

'''
- save_curfew_period: Guarda el periodo de toque de queda en el archivo "curfew_period.log"
- start_time: Hora de inicio del toque de queda (formato "HH:MM")
- end_time: Hora de fin del toque de queda (formato "HH:MM")
'''
def save_curfew_period(start_time : str, end_time : str) -> None:
    global curfew_period
    curfew_period = [start_time, end_time]
    
    try:
        with open("curfew_period.log", "w") as f:
            f.write(f"{start_time}\n")
            f.write(f"{end_time}\n")
    except Exception as e:
        print(f"Error al guardar el periodo de toque de queda: {e}")
        make_log("curf", success=False, details=f"Error al guardar el periodo de toque de queda: {e}")