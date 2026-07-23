def security_scan(*targets):
    for target in targets:
        print(f"\nScanning {target}")

        ports = [22, 80, 443]

        for port in ports:
           print(f"Checking port {port}")

security_scan(
    "192.168.1.10",
    "192.168.1.20"
)   