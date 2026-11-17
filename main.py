
#!/usr/bin/env python3
"""WIFOO - Wi-Fi discovery and wireless analysis interface."""

import json
from pathlib import Path

from modules.terminal_ui import banner, ask, info, warn, success
from modules.wifi_scanner import scan_wifi, security_label
from modules.fake_hacker import run_simulation
from modules.prank_link import choose_prank, open_link

CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config():
    try:
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        warn("Configuration unavailable.")
        return {"prank_pages": [], "open_browser": True}


def main():
    config = load_config()

    banner()
    info("WIFOO Wireless Intelligence Interface")
    info("Wireless discovery initialized.")

    networks = scan_wifi()

    if not networks:
        warn("Unable to retrieve wireless scan results.")
        return

    print("\n  AVAILABLE NETWORKS:\n")

    for i, net in enumerate(networks, 1):
        ssid = net.get("ssid") or "<Hidden network>"
        signal = net.get("level", "?")
        security = security_label(net.get("capabilities", ""))

        print(f"  [{i}] {ssid} | {security} | {signal} dBm")

    while True:
        raw = ask("\nSelect target (number / q): ").strip()

        if raw.lower() == "q":
            return

        if raw.isdigit() and 1 <= int(raw) <= len(networks):
            selected = networks[int(raw) - 1]
            break

        warn("Invalid selection.")

    ssid = selected.get("ssid") or "<Hidden network>"

    print(f"\n  Target   : {ssid}")
    print(f"  Security : {security_label(selected.get('capabilities', ''))}")
    print(f"  Signal   : {selected.get('level', 'N/A')} dBm")

    if ask("\nInitialize operation? (y/n): ").strip().lower() != "y":
        info("Operation cancelled.")
        return

    run_simulation(ssid)

    page = choose_prank(config.get("prank_pages", []))

    if not page:
        warn("Result page unavailable.")
        return

    success("OPERATION COMPLETED")
    info("Analysis sequence finished.")
    info("Result package generated.")

    print(f"\n  Result page: {page['url']}\n")

    if config.get("open_browser", True):
        if ask("Open result page? (y/n): ").strip().lower() == "y":
            open_link(page["url"])


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n  [!] Operation interrupted.")
