def vulnerability_report(**report):
    print("VULNERABILITY REPORT")
    print("--------------------")
    for key, value in report.items():
        print(f"{key}: {value}")
vulnerability_report(
    target="192.168.1.50",
    vulnerability="SQL Injection",
    severity="HIGH",
    status="OPEN",
    port=80,
    service="HTTP"
)
