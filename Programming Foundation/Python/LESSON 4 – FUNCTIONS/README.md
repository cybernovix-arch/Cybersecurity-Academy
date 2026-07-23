# 🐍 Lesson 4 - Functions

## Overview

This lesson introduces Python functions and how they help programmers organize, reuse, and maintain code.

Functions allow us to group instructions together and execute them whenever needed.

In cybersecurity programming, functions are important because security tools are usually built from many smaller reusable components.

Examples:

- Port scanning functions
- Log analysis functions
- File processing functions
- Report generation functions

---

# Learning Objectives

By the end of this lesson, I learned:

- What functions are
- Why functions are used
- How to create functions
- How to pass information into functions
- How to return data from functions
- How to use parameters
- How to use multiple arguments
- How to organize code using functions

---

# Key Concepts

## 1. Creating Functions

A function is created using the `def` keyword.

Example:

```python
def greet():
    print("Hello")
```

Calling the function:

```python
greet()
```

Output:

```
Hello
```

---

# 2. Function Parameters

Parameters allow functions to receive information.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

Calling:

```python
greet("Mohamed")
```

Output:

```
Hello Mohamed
```

---

# 3. Return Values

Functions can send data back using `return`.

Example:

```python
def add(a, b):
    return a + b
```

Usage:

```python
result = add(5, 3)
```

Result:

```
8
```

---

# 4. Multiple Arguments (*args)

`*args` allows a function to accept multiple values.

Example:

```python
def scan_ports(*ports):
    for port in ports:
        print(port)
```

Usage:

```python
scan_ports(21,22,80,443)
```

---

# 5. Functions and Cybersecurity

Functions are used everywhere in cybersecurity tools.

Example:

A vulnerability scanner may contain:

```
scanner.py

|
├── check_ports()
├── identify_services()
├── generate_report()
└── save_results()
```

Each function performs one specific task.

---

# Lesson 4 Final Project

## 🛡️ Modular Recon Tool

This project combined everything learned in Lessons 1-4.

Features:

- Python functions
- Parameters
- Return values
- Dictionaries
- Loops
- Conditions
- Modules
- Code organization

Project structure:

```
modular_recon_tool/

├── main.py
├── scanner.py
├── reporter.py
├── utils.py
└── README.md
```

---

# Skills Practiced

✅ Creating reusable functions  
✅ Passing data between functions  
✅ Returning results  
✅ Using `*args`  
✅ Organizing Python programs into modules  
✅ Building a small cybersecurity automation tool  

---

# Completion Status

✅ Lesson 4 Completed

✅ Final Project Completed

Project:

```
Modular Recon Tool v1.0
```

---

# Next Steps

Continue learning:

- File handling
- Error handling
- Automation scripts
- Security tool development
```