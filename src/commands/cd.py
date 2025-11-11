import os

def run(args):
    try:
        os.chdir(os.path.expanduser(args[0]))
    except FileNotFoundError:
        print(f"El directorio '{args[0]}' no existe")
    