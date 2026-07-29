import time

attempts = 0
correct_password = "secure123"
while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Access granted.")
        break
    else:
        print("Access denied. Try again.")
        attempts += 1
    if attempts == 3:
        print("Too many failed attempts. Access locked for 10 seconds.")
        for seconds in range(10,0,-1):
            print(f"{seconds} seconds remaining...", end="\r")
            time.sleep(2)
        attempts = 0  # Reset attempts after lockout
        print("You can try again now.")