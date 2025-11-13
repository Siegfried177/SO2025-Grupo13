import os

def set_current_dir(path : str) -> None:
    global previous_dir, current_dir
    previous_dir = current_dir
    current_dir = path

lang : str = "es"
commands_dict : dict[str, object] = {}
current_user : str = "cyaluk"
previous_dir : str = os.getcwd()
current_dir : str = os.getcwd()