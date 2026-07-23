from scanner import scan_ports
from reporter import generate_report
from utils import print_banner

def main():

    print_banner()

    target = "192.168.1.10"

    results = scan_ports(
        21,
        22,
        80,
        443,
        3306
    )

    generate_report(target, results)

if __name__ == "__main__":
    main()