ports = [21, 22, 25, 53, 80, 110, 143, 443]
open_ports = [21,110,143,443]
for port in ports:
    if port in open_ports:
        print(f"Port {port}: is open.")
    else:
        print(f"Port {port}: is closed.")