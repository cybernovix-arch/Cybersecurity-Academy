def scan_ports(*ports):
    for port in ports:
        print(f"Checking port {port}")

scan_ports(22, 80, 443, 8080)