def security_alert(ip, severity="LOW", status='NEW'):
    print(f"IP: {ip}")
    print(f"Severity: {severity}")
    print(f"Status: {status}")

security_alert("192.168.1.100")

security_alert("10.0.0.5", severity="HIGH", status="INVESTIGATING")