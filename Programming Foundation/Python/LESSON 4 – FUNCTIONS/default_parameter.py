#Default parameters must come after normal parameters.
def scan(ip,port=80):
    return f"Scanning {ip}:{port}..."
print(scan("192.168.1.100"))