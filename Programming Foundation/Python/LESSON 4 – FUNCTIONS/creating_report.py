def create_report(**incident):
    print("SECURITY INCIDENT REPORT")
    for key, value in incident.items():
        print(f"{key}: {value}")
create_report(
     ip="45.22.10.5",
    attack="Brute Force",
    severity="CRITICAL",
    username="admin",
    location="USA"
)