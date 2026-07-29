blocked_ip = "192.168.1.100"
incoming_ip = input("Enter the incoming IP address: ")

if incoming_ip == blocked_ip:
    print("Access denied. This IP address is blocked.")
else:
    print("Access granted.")