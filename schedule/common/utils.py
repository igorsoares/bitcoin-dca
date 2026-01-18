import os 
from schedule.configuration.setup_config_env import getenvs

colors_dict = {
    "yellow": "\033[33m",
    "red": "\033[31m",
    "green": "\033[32m",
    "reset": "\033[0m",
}

def print_yellow(message:str):
    print(f"{colors_dict['yellow']}{message}{colors_dict['reset']}")

def print_green(message:str):
    print(f"{colors_dict['green']}{message}{colors_dict['reset']}")

def print_colored(message: str, color_code: str = colors_dict['reset']):
    print(f"{color_code}{message}{colors_dict['reset']}")

def clear_console():
    os.system("clear")
