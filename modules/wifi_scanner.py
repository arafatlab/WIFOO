"""Read nearby Wi-Fi scan metadata through the official Termux:API bridge.
No passwords are requested, captured, tested, or stored.
"""
import json
import shutil
import subprocess

def security_label(capabilities):
    caps = (capabilities or "").upper()
    if "WPA3" in caps or "SAE" in caps:
        return "WPA3"
    if "WPA2" in caps:
        return "WPA2"
    if "WPA" in caps:
        return "WPA"
    if "WEP" in caps:
        return "WEP (legacy)"
    if caps:
        return "Open / Other"
    return "Unknown"

def scan_wifi():
    if not shutil.which("termux-wifi-scaninfo"):
        print("[!] termux-wifi-scaninfo not found.")
        print("    Install the Termux:API app and run: pkg install termux-api")
        return []
    try:
        result = subprocess.run(
            ["termux-wifi-scaninfo"],
            capture_output=True, text=True, timeout=20, check=False
        )
        if result.returncode != 0:
            print("[!] Wi-Fi scan failed. Check Android location / nearby-device permissions.")
            if result.stderr.strip():
                print("    " + result.stderr.strip().splitlines()[-1])
            return []
        data = json.loads(result.stdout or "[]")
        return data if isinstance(data, list) else []
    except (subprocess.TimeoutExpired, json.JSONDecodeError, OSError):
        print("[!] Could not read Wi-Fi scan results.")
        return []
