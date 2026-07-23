def security_scan(*targets):
    for target in targets:
        print(f"Starting scan: {target}")

security_scan(
    "192.168.1.10",
    "192.168.1.20",
    "10.0.0.5"
)