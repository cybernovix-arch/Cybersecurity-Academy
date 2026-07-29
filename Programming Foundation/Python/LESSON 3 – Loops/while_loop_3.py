attempts = 0
correct_password = "secure123"
while attempts < 3:
  user_input = input("Enter the password: ")
  if user_input == correct_password:
    print("Access granted.")
    break
  else:
    print("Access denied. Try again.") 
    attempts += 1
  if attempts == 3:
    print("Too many failed attempts. Access locked.")