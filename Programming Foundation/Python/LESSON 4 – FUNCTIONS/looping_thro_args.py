def scan_targets(*targets):
    for target in targets:
        print(f"Scanning {target}")

scan_targets("192.168.1.1", "192.168.1.2", "192.168.1.3")
