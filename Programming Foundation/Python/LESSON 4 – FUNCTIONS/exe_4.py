user_password = input("Enter your password: ")

def check_password(user_password):
    if len(user_password) < 8:
        return "Password must be at least 8 characters"
    elif not any(char.islower() for char in user_password):
        return "Needs lowercase letters"
    elif not any(char.isupper() for char in user_password):
        return "Needs uppercase letters"
    elif not any(char.isdigit() for char in user_password):
        return "Needs at least one digit"
    else:
        return "Strong password"
print(check_password(user_password))