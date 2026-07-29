correct_password = "secure123"
user_input = input("Enter the password: ")

if user_input == correct_password:
    print("Access granted.")
else:
    print("Access denied. Incorrect password.")