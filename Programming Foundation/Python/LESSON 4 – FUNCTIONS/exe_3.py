password = input("Enter your password: ")
def check_password(password):
    if len(password) >= 8:
        
        return "Strong password"
    else:
        return "Weak password"
print(check_password(password))
    
