def scan(network, *ips, **options):

    print(f"Scanning Network: {network}")

    print(f"IP Addresses:")
    for ip in ips:
        print(ip)
    
    print(f"Options:")
    for key, value in options.items():
        print(f"{key}: {value}")

scan(
    "192.168.1.0/24",
    "192.168.1.10",
    "192.168.1.20",
    scan_type="full",
    timeout=10
)
