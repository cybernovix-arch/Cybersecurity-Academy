# To modify global variables inside a function, you need to use the 'global' keyword. This tells Python that you want to use the global variable instead of creating a new local variable with the same name. = "192.168.1.1"

counter = 0 # Global variable

def increase():
    global counter
    counter += 1
    print(counter)

increase()
