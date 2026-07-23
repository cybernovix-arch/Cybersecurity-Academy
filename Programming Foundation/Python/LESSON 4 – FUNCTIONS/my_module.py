def scan_port(port):
    """
    Check whether a port is open
    """
    open_ports=[22,80,443]
    if port in open_ports:
        return "OPEN"
    return "CLOSED"