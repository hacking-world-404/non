from os import system as c
import time
import random

# Colour Codes
A = '\033[1;97m'
R = '\033[1;31m'
Y = '\033[1;33m'
G = '\033[1;32m'
C = '\033[1;36m'

# Logo Function
def logo():
    c('clear')
    print(f"""{R}
██████╗  █████╗ ███╗   ██╗███████╗
██╔══██╗██╔══██╗████╗  ██║██╔════╝
██████╔╝███████║██╔██╗ ██║█████╗  
██╔═══╝ ██╔══██║██║╚██╗██║██╔══╝  
██║     ██║  ██║██║ ╚████║███████╗
╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝
    {Y}HACKING WORLD - PHONE FLASH PRANK
{A}-----------------------------------------
""")

# Animation Function
def animation(msg):
    for x in msg:
        print(x, end='', flush=True)
        time.sleep(0.03)
    print()

# Main Tool
def flash_tool():
    logo()
    ip = input(f"{C}[+] Enter Target IP Address: ")
    print(f"{Y}\n[!] Checking Device Root Access...")
    time.sleep(2)
    print(f"{R}[×] Root Access Denied!\n")
    time.sleep(1)
    print(f"{Y}[+] Attempting Bypass Security...")
    time.sleep(3)

    animation(f"{G}\n[*] Connecting to {ip}...")
    time.sleep(1)
    animation(f"{G}[*] Bypass Success.")
    time.sleep(1)

    print(f"{Y}\n[+] Starting Flash Process...\n")
    for i in range(1, 101, 10):
        print(f"{C}Flashing... {i}%")
        time.sleep(0.5)
    print(f"{G}\n[✓] Flash Complete for {ip}!\n")
    input(f"{A}Press Enter to Exit...")

# Run Tool
flash_tool()