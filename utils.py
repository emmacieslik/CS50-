import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def quit_program():
    clear_screen()
    print("Valar Morghulis.\n")
    sys.exit()
