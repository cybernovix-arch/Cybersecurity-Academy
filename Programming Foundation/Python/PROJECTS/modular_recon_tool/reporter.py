def generate_report(target, results):
    """
    Generate a security scan report
    Args:
        target (str): Target identifier.
        results (dict): Simulated port scan results.

    Returns:
        None
    """
    print("\n===== SECURITY SCAN REPORT =====")
    print(f"Target: {target}")
    print("--------------------------------")

    for port, status in results.items():
        print(f"Port {port}: {status}")

    print("--------------------------------")
