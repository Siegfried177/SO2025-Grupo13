from utils.var import restricted_commands, SHELL_DIR
from utils.log_gen import make_log
from utils import var
from datetime import datetime, time
from utils.lang_manager import t

'''
- load_curfew: Carga la configuración del toque de queda
'''
def load_curfew() -> None:
    load_restricted_commands() # Cargar lista de comandos restringidos
    load_curfew_period() # Cargar periodo de toque de queda
    
    curfew_file = SHELL_DIR / "curfew.log"
    
    try: # Cargar estado del toque de queda
        with curfew_file.open("r") as f: # Se abre el archivo para saber el estado del toque de queda (on / off)
            curfew_state = f.readline().strip()[0] # Se lee el primer caracter del archivo
            var.curfew_on = (curfew_state == "1")  # Toque de queda activado si es "1", desactivado si es "0"
            
    except FileNotFoundError:
        print(t("curf_load_missing_curfew_log"))
        make_log("curf", success=False, details="El archivo 'curfew.log' no existe, se creará uno")
        
        var.curfew_on = True  # Toque de queda activado por defecto
        
        with curfew_file.open("w") as f: # Se crea el archivo con los comandos por defecto
            f.write("1\n")  # Toque de queda activado por defecto
            
'''
- save_curfew: Guarda el estado del toque de queda (on / off)
'''
def save_curfew() -> None:
    curfew_file = SHELL_DIR / "curfew.log"
    
    try: 
        with curfew_file.open("w") as f: # Se abre el archivo para saber el estado del toque de queda (on / off)
            f.write(f"{1 if var.curfew_on else 0}\n")  # Guardar el estado del toque de queda
            
    except FileNotFoundError:
        print(t("curf_load_missing_curfew_log"))
        make_log("curf", success=False, details="El archivo 'curfew.log' no existe, se creará uno")
        
        with curfew_file.open("w") as f: # Se crea el archivo con los comandos por defecto
            f.write(f"{1 if var.curfew_on else 0}\n")  # Toque de queda activado por defecto

'''
- load_restricted_commands: Carga la lista de comandos restringidos desde el archivo "restricted_cmds.log"
'''
def load_restricted_commands() -> None:
    restricted_file = SHELL_DIR / "restricted_cmds.log"
    
    try:
        with restricted_file.open("r") as f: # Se abre el archivo y se lee la lista de comandos restringidos
            var.restricted_commands = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(t("curf_load_missing_restricted_cmds"))
        make_log("curf", success=False, details="El archivo 'restricted_cmds.log' no existe, se creará uno con los comandos por defecto")
        var.restricted_commands = ["rm"]  # Comando restringido por defecto, cp no está por que solo está restringido en parte
        
        with restricted_file.open("w") as f: # Se crea el archivo con los comandos por defecto
            for cmd in var.restricted_commands:
                f.write(cmd + "\n")

'''
- save_restricted_commands: Guarda la lista de comandos restringidos en el archivo "restricted_cmds.log"
'''
def save_restricted_commands() -> None:
    restricted_file = SHELL_DIR / "restricted_cmds.log"
    
    try:
        with restricted_file.open("w") as f:
            for cmd in var.restricted_commands:
                f.write(cmd + "\n")
    except Exception as e:
        print(t("curf_error_saving_restricted_cmds"))
        make_log("curf", success=False, details=f"Error al guardar la lista de comandos restringidos: {e}")

'''
- load_curfew_period: Carga el periodo de toque de queda desde el archivo "curfew_period.log"
'''
def load_curfew_period() -> None:
    period_file = SHELL_DIR / "curfew_period.log"
    
    try:
        with period_file.open("r") as f:
            lines = [line.strip() for line in f if line.strip()]
            if len(lines) >= 2:
                var.curfew_period = [lines[0], lines[1]]
    except FileNotFoundError:
        print(t("curf_load_missing_period"))
        make_log("curf", success=False, details="El archivo 'curfew_period.log' no existe, se creará uno con el periodo por defecto")
        var.curfew_period = ["22:00", "06:00"]  # Periodo por defecto
        
        with period_file.open("w") as f: # Se crea el archivo con el periodo por defecto
            f.write(f"{var.curfew_period[0]}\n")
            f.write(f"{var.curfew_period[1]}\n")

'''
- save_curfew_period: Guarda el periodo de toque de queda en el archivo "curfew_period.log"
-- start_time: Hora de inicio del toque de queda (formato "HH:MM")
-- end_time: Hora de fin del toque de queda (formato "HH:MM")
'''
def save_curfew_period(start_time : str, end_time : str) -> None:
    var.curfew_period = [start_time, end_time]
    period_file = SHELL_DIR / "curfew_period.log"
    
    try:
        with period_file.open("w") as f:
            f.write(f"{start_time}\n")
            f.write(f"{end_time}\n")
    except Exception as e:
        print(t("curf_error_saving_period"))
        make_log("curf", success=False, details=f"Error al guardar el periodo de toque de queda: {e}")

'''
- is_in_curfew: Verifica si la hora actual está dentro del periodo de toque de queda
- return: True si está en toque de queda, False en caso contrario
'''
def is_in_curfew() -> bool:
    if not var.curfew_on:
        return False
    
    start_hour, start_minute = map(int, var.curfew_period[0].split(":"))
    end_hour, end_minute = map(int, var.curfew_period[1].split(":"))

    start_time = time(start_hour, start_minute)
    end_time = time(end_hour, end_minute)

    current_time = datetime.now().time()
    if start_time <= end_time:
        return start_time <= current_time <= end_time
    else:
        return current_time >= start_time or current_time <= end_time