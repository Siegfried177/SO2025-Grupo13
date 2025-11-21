from utils import curfew_utils, var
from utils.log_gen import make_log

'''
- curf: Maneja el sistema de toque de queda y los comandos restringidos en ese periodo (Mostrar o cambiar el periodo de horas, activar/desactivar)
- args: Ninguno
        [Horas en formato 24h "HH:MM HH:MM" para cambiar el periodo]
        [on]
        [off]
        [add] [comando]
        [rmv] [comando]
        [list]
-- Muestra el periodo actual de toque de queda si no se proporcionan argumentos y está activado
-- Cambia el periodo de toque de queda si se proporcionan horas válidas
-- Activa o desactiva el toque de queda si se proporcionan "on" o "off" (es case-sensitive)
-- add y rmv añaden / eliminan comandos de la lista de comandos restringidos durante el toque de queda, rm y cp están restringidos por defecto y no se puede cambiar
-- list muestra la lista de comandos restringidos durante el toque de queda
'''
def run(args : list[str]) -> None:
    if len(args) > 2: # Demasiados argumentos
        print("Error: Demasiados argumentos para 'curf'")
        make_log("curf", success=False, details="Demasiados argumentos para 'curf'")
        return
    
    if len(args) == 0: # Mostrar toque de queda actual
        if not var.curfew_on:
            print("El toque de queda está desactivado")
            make_log("curf", details="Toque de queda está desactivado")
            return
        print(f"Periodo de restricción: {var.curfew_period[0]} - {var.curfew_period[1]}")
        make_log("curf", details="Mostrando periodo de toque de queda")
        return
    
    if len(args) == 1:
        if args[0] == "--help": # Mostrar ayuda
            print("Uso: curf [on | off | add <comando> | rmv <comando> | list | <HH:MM HH:MM>]")
            print("Gestiona el sistema de toque de queda y los comandos restringidos durante ese periodo")
            print("Sin argumentos: Muestra el periodo actual de toque de queda si está activado")
            print("on: Activa el toque de queda.")
            print("off: Desactiva el toque de queda.")
            print("add <comando>: Añade un comando a la lista de comandos restringidos durante el toque de queda")
            print("rmv <comando>: Elimina un comando de la lista de comandos restringidos durante el toque de queda")
            print("list: Muestra la lista de comandos restringidos durante el toque de queda")
            print("<HH:MM HH:MM>: Cambia el periodo de toque de queda a las horas especificadas")
            print("cp está parcialmente restringido, no se puede usar para sobreescribir archivos durante el toque de queda")
            make_log("curf --help", details="Mostrando ayuda para 'curf'")
            return
        
        elif args[0] == "on": # Activar toque de queda
            if (var.curfew_on):
                print("El toque de queda ya está activado")
                make_log("curf on", success=False, details="Toque de queda ya estaba activado")
                return
            var.curfew_on = True
            print("Toque de queda activado")
            make_log("curf on", details="Toque de queda activado")
            return
        
        elif args[0] == "off": # Desactivar toque de queda
            if (not var.curfew_on):
                print("El toque de queda ya está desactivado")
                make_log("curf off", success=False, details="Toque de queda ya estaba desactivado")
                return
            var.curfew_on = False
            print("Toque de queda desactivado")
            make_log("curf off", details="Toque de queda desactivado")
            return
        
        elif args[0] == "list": # Mostrar lista de comandos restringidos
            print ("- cp") # Comando restringido parcialmente pero igualmente se muestra
            for cmd in var.restricted_commands:
                print(f"- {cmd}")
            make_log("curf list", details="Mostrando lista de comandos restringidos durante el toque de queda")
            return
        
        else: # Argumento inválido
            print("Error: Argumento inválido para 'curf'")
            make_log("curf", success=False, details="Argumento inválido para 'curf'")
            return
        
    if len(args) == 2:
        if args[0] == "add": # Añadir un comando a la lista de restringidos
            cmd_to_add = args[1]
            
            if cmd_to_add in var.restricted_commands:
                print(f"El comando '{cmd_to_add}' ya está en la lista de comandos restringidos")
                make_log("curf add", success=False, details=f"Comando '{cmd_to_add}' ya estaba restringido")
                return
            if cmd_to_add in var.restricted_commands or cmd_to_add == "cp":
                print(f"El comando '{cmd_to_add}' no se puede restringir")
                make_log("curf add", success=False, details=f"Comando '{cmd_to_add}' no se puede restringir")
                return
            
            curfew_utils.save_restricted_commands()
            print(f"Comando '{cmd_to_add}' añadido a la lista de comandos restringidos")
            make_log("curf add", details=f"Comando '{cmd_to_add}' añadido a la lista de comandos restringidos")
            return
        
        if args[0] == "rmv": # Eliminar un comando de la lista de restringidos
            cmd_to_rmv = args[1]
            
            if cmd_to_rmv not in var.restricted_commands:
                print(f"El comando '{cmd_to_rmv}' no está en la lista de comandos restringidos")
                make_log("curf rmv", success=False, details=f"Comando '{cmd_to_rmv}' no estaba restringido")
                return
            if cmd_to_rmv in var.restricted_commands or cmd_to_rmv == "cp":
                print(f"El comando '{cmd_to_rmv}' no se puede eliminar de la lista de restringidos")
                make_log("curf rmv", success=False, details=f"Comando '{cmd_to_rmv}' no se puede eliminar de la lista de restringidos")
                return
            
            var.restricted_commands.remove(cmd_to_rmv)
            print(f"Comando '{cmd_to_rmv}' eliminado de la lista de comandos restringidos")
            make_log("curf rmv", details=f"Comando '{cmd_to_rmv}' eliminado de la lista de comandos restringidos")
            return
        
        try:
            start_time = args[0]
            end_time = args[1]
            
            for t in [start_time, end_time]: # Validar formato HH:MM
                hh, mm = t.split(":")
                hh = int(hh)
                mm = int(mm)
                
                if hh < 0 or hh > 23 or mm < 0 or mm > 59:
                    raise ValueError
            
            var.curfew_period = [start_time, end_time]
            curfew_utils.save_curfew_period(start_time, end_time)
            print(f"Periodo de toque de queda cambiado a: {start_time} - {end_time}")
            make_log("curf", details=f"Periodo de toque de queda cambiado a: {start_time} - {end_time}")
        except ValueError: # Formato de hora inválido
            print("Error: Formato de hora inválido. Debe ser 'HH:MM HH:MM'")
            make_log("curf", success=False, details="Formato de hora inválido para 'curf'")