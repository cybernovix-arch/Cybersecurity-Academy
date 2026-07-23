#*args allows a function to accept any number of positional arguments.

def scan_ports(*ports):
    print("Scanning ports:", ports)
scan_ports(22, 80, 443)
