ips = [
    "192.168.1.1",
    "192.168.1.2",
    "192.168.1.3"
]

ports = [22, 80, 443, 8080]

for ip in ips:
    print(f"\nScanning {ip}")

    for port in ports:
        print(f" Checking port {port}")
