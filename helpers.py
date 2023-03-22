import re
import os
import platform
from colorama import *
from termcolor import colored, cprint
init(autoreset=True)


def limpiar_pantalla() -> None:
    os.system('cls') if platform.system() == "Windows" else os.system('clear')