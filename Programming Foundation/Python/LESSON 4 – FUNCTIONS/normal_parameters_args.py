#Normal parameters come first

def scan(network, *targets):
    print(f"Scanning network: {network}")

    for target in targets:
        print(f"Scanning target: {target}")

scan("192.168.1.0/24", "192.168.1.1", "192.168.1.2", "192.168.1.3")