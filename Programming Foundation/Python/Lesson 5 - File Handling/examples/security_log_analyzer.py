failed_attempts = 0
print("\n===== SUSPICIOUS LOGIN EVENTS =====\n")
with open("auth.log", "r") as file:
    for line in file:
        if "Failed login" in line:
            print(line.strip())
            failed_attempts += 1

print("\n-----------------------------------")
print(f"Total failed login attempts: {failed_attempts}\n")
