from utils import curfew_utils, var
from utils.log_gen import make_log
from utils.lang_manager import t

'''
- curf: Maneja el sistema de toque de queda y los comandos restringidos en ese periodo (Mostrar o cambiar el periodo de horas, activar/desactivar)
- args: Ninguno
        [Horas en formato 24h "HH:MM HH:MM" para cambiar el periodo]
        [on]
        [off]
        [add] [comando]
        [rmv] [comando]
        [list]
        [--help]
-- Muestra el periodo actual de toque de queda si no se proporcionan argumentos y está activado
-- Cambia el periodo de toque de queda si se proporcionan horas válidas
-- Activa o desactiva el toque de queda si se proporcionan "on" o "off" (es case-sensitive)
-- add y rmv añaden / eliminan comandos de la lista de comandos restringidos durante el toque de queda, rm y cp están restringidos por defecto y no se puede cambiar
-- list muestra la lista de comandos restringidos durante el toque de queda
-- --help muestra la ayuda del comando
'''
def run(args : list[str]) -> None:
    if len(args) > 2: # Demasiados argumentos
        print(t("curf_too_many_args"))
        make_log("curf", success=False, details="Demasiados argumentos para 'curf'")
        return
    
    if len(args) == 0: # Mostrar toque de queda actual
        if not var.curfew_on:
            print(t("curf_is_off"))
            make_log("curf", details="Toque de queda está desactivado")
            return
        print(t("curf_period").format(var.curfew_period[0], var.curfew_period[1]))
        make_log("curf", details="Mostrando periodo de toque de queda")
        return
    
    if len(args) == 1:
        if args[0] == "--help": # Mostrar ayuda
            print(t("curf_help_usage"))
            print(t("curf_help_manage"))
            print(t("curf_help_no_args"))
            print(t("curf_help_on"))
            print(t("curf_help_off"))
            print(t("curf_help_add"))
            print(t("curf_help_rmv"))
            print(t("curf_help_list"))
            print(t("curf_help_hours"))
            print(t("curf_help_cp_restricted"))
            make_log("curf --help", details="Mostrando ayuda para 'curf'")
            return
        
        elif args[0] == "on": # Activar toque de queda
            if (var.curfew_on):
                print(t("curf_already_on"))
                make_log("curf on", success=False, details="Toque de queda ya estaba activado")
                return
            
            var.curfew_on = True
            print(t("curf_now_on"))
            make_log("curf on", details="Toque de queda activado")
            return
        
        elif args[0] == "off": # Desactivar toque de queda
            if (not var.curfew_on):
                print(t("curf_already_off"))
                make_log("curf off", success=False, details="Toque de queda ya estaba desactivado")
                return
            
            var.curfew_on = False
            curfew_utils.save_curfew()
            print(t("curf_now_off"))
            make_log("curf off", details="Toque de queda desactivado")
            return
        
        elif args[0] == "list": # Mostrar lista de comandos restringidos
            print(t("curf_list_cp"))
            for cmd in var.restricted_commands:
                print(f"- {cmd}")
            make_log("curf list", details="Mostrando lista de comandos restringidos durante el toque de queda")
            return
        
        else: # Argumento inválido
            print(t("curf_invalid_arg"))
            make_log("curf", success=False, details="Argumento inválido para 'curf'")
            return
        
    if len(args) == 2:
        if args[0] == "add": # Añadir un comando a la lista de restringidos
            cmd_to_add = args[1]
            
            if cmd_to_add in var.restricted_commands or cmd_to_add == "cp":
                print(t("curf_add_exists").format(cmd_to_add))
                make_log("curf add", success=False, details=f"Comando '{cmd_to_add}' ya estaba restringido")
                return
            if cmd_to_add == "curf": # Para evitar problemas con el propio comando curf, este no se puede restringir
                print(t("curf_add_forbidden").format(cmd_to_add))
                make_log("curf add", success=False, details=f"Comando '{cmd_to_add}' no se puede restringir")
                return
            
            var.restricted_commands.append(cmd_to_add)
            curfew_utils.save_restricted_commands()
            print(t("curf_add_success").format(cmd_to_add))
            make_log("curf add", details=f"Comando '{cmd_to_add}' añadido a la lista de comandos restringidos")
            return
        
        if args[0] == "rmv": # Eliminar un comando de la lista de restringidos
            cmd_to_rmv = args[1]
            
            if cmd_to_rmv not in var.restricted_commands:
                print(t("curf_rmv_not_exists").format(cmd_to_rmv))
                make_log("curf rmv", success=False, details=f"Comando '{cmd_to_rmv}' no estaba restringido")
                return
            if cmd_to_rmv == "rm" or cmd_to_rmv == "cp":
                print(t("curf_rmv_forbidden").format(cmd_to_rmv))
                make_log("curf rmv", success=False, details=f"Comando '{cmd_to_rmv}' no se puede eliminar de la lista de restringidos")
                return
            
            var.restricted_commands.remove(cmd_to_rmv)
            print(t("curf_rmv_success").format(cmd_to_rmv))
            make_log("curf rmv", details=f"Comando '{cmd_to_rmv}' eliminado de la lista de comandos restringidos")
            return
        
        try:
            start_time = args[0]
            end_time = args[1]
            
            for time in [start_time, end_time]: # Validar formato HH:MM
                hh, mm = time.split(":")
                hh = int(hh)
                mm = int(mm)
                
                if hh < 0 or hh > 23 or mm < 0 or mm > 59:
                    raise ValueError
            
            curfew_utils.save_curfew_period(start_time, end_time)
            print(t("curf_period_changed").format(start_time, end_time))
            make_log("curf", details=f"Periodo de toque de queda cambiado a: {start_time} - {end_time}")
        except ValueError: # Formato de hora inválido
            print(t("curf_invalid_time_format"))
            make_log("curf", success=False, details="Formato de hora inválido para 'curf'")
