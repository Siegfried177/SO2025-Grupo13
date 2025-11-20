from utils import var
from utils.log_gen import make_log

'''
- curf: Maneja el sistema de toque de queda (Mostrar o cambiar el periodo de horas, activar/desactivar)
- args: Ninguno
        [Horas en formato 24h "HH:MM HH:MM" para cambiar el periodo]
        [on]
        [off]
-- Muestra el periodo actual de toque de queda si no se proporcionan argumentos y está activado
-- Cambia el periodo de toque de queda si se proporcionan horas válidas
-- Activa o desactiva el toque de queda si se proporcionan "on" o "off" (es case-sensitive)
'''
def run(args : list[str]) -> None:
    if len(args) > 2:
        print("Error: Demasiados argumentos para 'curf'")
        make_log("curf", success=False, details="Demasiados argumentos para 'curf'")
        return
    
    if len(args) == 0:
        if not var.curfew_on:
            print("El toque de queda está desactivado")
            make_log("curf", details="Toque de queda está desactivado")
            return
        print(f"Periodo de restricción: {var.curfew_period[0]} - {var.curfew_period[1]}")
        make_log("curf", details="Mostrando periodo de toque de queda")
        return
    
    if len(args) == 1:
        if args[0] == "on":
            if (var.curfew_on):
                print("El toque de queda ya está activado")
                make_log("curf on", success=False, details="Toque de queda ya estaba activado")
                return
            var.curfew_on = True
            print("Toque de queda activado")
            make_log("curf on", details="Toque de queda activado")
            return
        
        elif args[0] == "off":
            if (not var.curfew_on):
                print("El toque de queda ya está desactivado")
                make_log("curf off", success=False, details="Toque de queda ya estaba desactivado")
                return
            var.curfew_on = False
            print("Toque de queda desactivado")
            make_log("curf off", details="Toque de queda desactivado")
            return
        
        else:
            print("Error: Argumento inválido para 'curf'")
            make_log("curf", success=False, details="Argumento inválido para 'curf'")
            return
        
    if len(args) == 2:
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
            print(f"Periodo de toque de queda cambiado a: {start_time} - {end_time}")
            make_log("curf", details=f"Periodo de toque de queda cambiado a: {start_time} - {end_time}")
        except ValueError: # Formato de hora inválido
            print("Error: Formato de hora inválido. Debe ser 'HH:MM HH:MM'")
            make_log("curf", success=False, details="Formato de hora inválido para 'curf'")