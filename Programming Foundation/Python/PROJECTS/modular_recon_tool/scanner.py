def scan_ports(*ports):

    """
    Simulate checking multiple network ports.

    Args:
        *ports: Any number of port numbers.

    Returns:
        dict: A dictionary containing each port and its simulated status.
    """

    open_ports = [22,80,443]
    results = {}
    for port in ports:
        if port in open_ports:
            results[port] = "OPEN"
        else:
            results[port] = "CLOSED"
    return results


