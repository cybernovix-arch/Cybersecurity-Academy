def security_alert(**alerts):
    for key, value in alerts.items():
        print(f"{key}: {value}")
security_alert(
    ip="192.168.1.100",
    severity="HIGH",
    status="BLOCKED"
)