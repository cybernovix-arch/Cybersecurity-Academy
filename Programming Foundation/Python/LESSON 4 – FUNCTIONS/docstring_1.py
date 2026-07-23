def security_alert(ip, severity="LOW", status="NEW"):
    """
    Create and display a security alert.

    Args:
        ip (str): IP address associated with the alert.
        severity (str): Severity level of the alert.
        status (str): Current status of the alert.

    Returns:
        None
    """

    print(f"IP: {ip}")
    print(f"Severity: {severity}")
    print(f"Status: {status}")