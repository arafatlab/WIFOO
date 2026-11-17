"""Purely theatrical terminal animation. It does not perform network actions."""
import random
import time
from modules.terminal_ui import GREEN, CYAN, YELLOW, RESET

def run_simulation(ssid):
    print("\n" + CYAN + "[*] Initializing cinematic simulation..." + RESET)
    steps = [
        "Resolving target label",
        "Analyzing broadcast security metadata",
        "Building imaginary handshake",
        "Decrypting absolutely nothing",
        "Generating prank result"
    ]
    for step in steps:
        print(GREEN + "[+] " + step + "..." + RESET)
        time.sleep(0.65)
        print("    " + "".join(random.choice("01ABCDEF") for _ in range(34)))
    for pct in (13, 27, 46, 68, 84, 100):
        bar = "#" * (pct // 5) + "-" * (20 - pct // 5)
        print(f"\r{YELLOW}[{bar}] {pct:3d}%{RESET}", end="", flush=True)
        time.sleep(0.35)
    print("\n\n" + GREEN + "[✓] SIMULATION FINISHED" + RESET)
    print(YELLOW + "    No Wi-Fi password was obtained. This is the prank part. 🐸" + RESET)
