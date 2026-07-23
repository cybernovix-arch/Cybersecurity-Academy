ports = [22, 23, 80, 443, 8080, 3306, 4089,5500]
open_ports = [22, 80, 443, 8080]

def scan_port(port):
    if port in open_ports:
        return f"Port {port} is OPEN"
    else:
        return f"Port {port} is CLOSED"

for port in ports:
    result = scan_port(port)
    print(result)