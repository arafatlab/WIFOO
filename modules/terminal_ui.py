import os
import shutil

GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"
BOLD = "\033[1m"

def clear():
    os.system("clear" if os.name == "posix" else "cls")

def banner():
    clear()
    print(CYAN + BOLD + r"""
 __        ___ _____ ___   ___
 \ \      / / |_   _/ _ \ / _ \
  \ \ /\ / /    | || | | | | | |
   \ V  V /     | || |_| | |_| |
    \_/\_/      |_| \___/ \___/
""" + RESET)
    print(GREEN + "       Wi-Fi discovery & prank simulator" + RESET)
    print("       ----------------------------------\n")

def ask(prompt):
    return input(YELLOW + prompt + RESET)

def info(message):
    print(CYAN + "[i] " + message + RESET)

def warn(message):
    print(YELLOW + "[!] " + message + RESET)

def success(message):
    print(GREEN + "[+] " + message + RESET)
