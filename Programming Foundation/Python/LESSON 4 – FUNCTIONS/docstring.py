#A docstring is documentation written inside a function, class, or module.
def scan_port(port):

    """
    Check a port and return its status
    """

    open_ports = [22,80,443]

    for port in open_ports:
        return "OPEN"
    else:
        return "CLOSED"
    
#print(scan_port.__doc__)

help(scan_port)
