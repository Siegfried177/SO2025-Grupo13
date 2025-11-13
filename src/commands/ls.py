import os 

def run(args):
    if len(args) > 2:  # Demasiados argumentos
        print("Demasiados argumentos para 'ls'")
        return
    
    if len(args) == 0:
        list_dir : list = os.listdir()
        list_dir = [item for item in list_dir if not item.startswith('.')]
        for item in list_dir:
            print(item)
        return
    
    hidden_items : bool = True if args[0] == "-a" else False
    
    if len(args) == 2:
        if hidden_items:
            list_dir : list = os.listdir(args[1])
            try:
                for item in list_dir:
                    print(item)
            except FileNotFoundError:
                print(f"No existe el directorio '{args[1]}'")
        else:
            print(f"Argumento/s no reconocido/s para 'ls'")
    
    elif len(args) == 1:
        if hidden_items:
            list_dir : list = os.listdir()
            try:
                for item in list_dir:
                    print(item)
            except FileNotFoundError:
                print(f"No existe el directorio '{args[0]}'")
        else:
            list_dir = os.listdir(args[0])
            list_dir = [item for item in list_dir if not item.startswith('.')]
            try:
                for item in list_dir:
                    print(item)
            except FileNotFoundError:
                print(f"No existe el directorio '{args[0]}'")