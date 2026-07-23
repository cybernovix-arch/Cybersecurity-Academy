def scan_port(port, service="Unknown"):
    print(f"Port {port} - {service}")
scan_port(22, "SSH")
scan_port(443, "HTTPS")
scan_port(3306)