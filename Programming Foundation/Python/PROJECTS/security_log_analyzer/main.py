def analyze_log():
    
    """
    Analyze an authentication log for failed login attempts.
    """

    failed_attempts = 0
    failed_events = []
    with open("auth.log","r") as file:
        for line in file:
            if "Failed login" in line:
                failed_events.append(line.strip())
                failed_attempts += 1
    return failed_events, failed_attempts


def display_report(failed_events, failed_attempts):

    """
    Display the security analysis report.
    """

    print("\n===== SECURITY LOG ANALYSIS =====")
    for event in failed_events:
        print(event)
    print("-----------------------------------")
    print(f"Total failed attempts: {failed_attempts}")


def save_report(failed_events, failed_attempts):

    """
    Save the security analysis report to a file.
    """
     
    with open("report.txt", "w") as file:
        file.write("===== SECURITY LOG ANALYSIS =====\n\n")
        for event in failed_events:
            file.write(event+"\n")
        file.write("--------------------------------\n")
        file.write(f"Total Failed Attempts: {failed_attempts}\n")


def main():
    failed_events, failed_attempts = analyze_log()

    display_report(failed_events, failed_attempts)

    save_report(failed_events, failed_attempts)


if __name__ == "__main__":
    main()