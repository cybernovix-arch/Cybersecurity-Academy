def scan_ports(*ports):

    open_ports = [22, 80, 443]
    
    for port in ports:
        if port in open_ports:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")

scan_ports(22, 23, 80, 443, 8080, 3306)

        