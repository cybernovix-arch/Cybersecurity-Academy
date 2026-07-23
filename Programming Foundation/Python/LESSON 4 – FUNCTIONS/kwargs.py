#**kwargs allows a function to accept any number of keyword arguments.

def security_alert(**alerts):
    print(alerts)
security_alert(
    ip = "192.168.1.100",
    severity = "HIGH",
    status = "BLOCKED"
)
  
