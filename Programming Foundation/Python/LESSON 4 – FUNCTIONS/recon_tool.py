def get_target():
    target = "192.168.1.100"
    return target

def scan_target():
    target = get_target()
    print(f"Scanning {target}...")

scan_target()
