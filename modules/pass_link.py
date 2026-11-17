import random
import shutil
import subprocess
import webbrowser

def choose_prank(pages):
    valid = [
        p for p in pages
        if isinstance(p, dict) and p.get("url", "").startswith(("https://", "http://"))
    ]
    return random.choice(valid) if valid else None

def open_link(url):
    if shutil.which("termux-open-url"):
        subprocess.Popen(["termux-open-url", url])
    else:
        webbrowser.open(url)
