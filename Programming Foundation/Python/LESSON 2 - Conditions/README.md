# Lesson 2 - Conditions (Decision Making)

## Objective

The objective of this lesson is to understand how programs make decisions using conditions.

I learned how to use:

- if statements
- else statements
- comparison operators
- Boolean values (True and False)

---

# What are Conditions?

A condition is a question that a program checks to decide what action to perform.

A condition produces one of two results:

- True
- False

Example:

```python
if condition:
    do something
else:
    do something else
```

---

# Why Do Conditions Exist?

Programs need conditions because they must react differently depending on situations.

Without conditions, programs would always perform the same action.

Examples:

- Login systems checking passwords.
- Firewalls deciding whether to allow or block traffic.
- Antivirus software detecting malicious files.
- Access control systems checking permissions.

---

# How Conditions Work

A computer evaluates a condition:

```
Question
   |
   |
 Is it True?
   |
 ----------------
 |              |
Yes             No
 |              |
Run action    Run else
```

Example:

```python
age = 19

if age >= 18:
    print("Access granted")
else:
    print("Access denied")
```

---

# Comparison Operators Learned

| Operator | Meaning | Example |
|----------|---------|---------|
| == | Equal to | password == "1234" |
| != | Not equal to | username != "admin" |
| > | Greater than | attempts > 5 |
| < | Less than | score < 50 |
| >= | Greater than or equal | age >= 18 |
| <= | Less than or equal | attempts <= 3 |

---

# Code Examples

## Access Control Example

```python
security_clearance = True

if security_clearance:
    print("Access granted")
else:
    print("Access denied")
```

Output:

```
Access granted
```

---

## Password Checker Example

```python
correct_password = "secure123"
user_input = input("Enter the password: ")

if user_input == correct_password:
    print("Access granted.")
else:
    print("Access denied. Incorrect password.")
```

---

# Cybersecurity Applications

Conditions are used in:

## Firewalls

Example:

```
IF IP address is blocked:

    Drop connection

ELSE:

    Allow connection
```

---

## Authentication Systems

Example:

```
IF username AND password are correct:

    Allow login

ELSE:

    Reject login
```

---

## Security Monitoring

Example:

```
IF failed login attempts >= 5:

    Lock account
```

---

# Files

- L2_conditions.py
- comparison_practice.py
- README.md

---

# What I Learned

In this lesson I learned:

- How programs make decisions.
- How if and else statements work.
- How comparison operators compare values.
- How Boolean values control program decisions.
- Why conditions are important in cybersecurity.

---

# Challenges Completed

✅ Created an access control program.

✅ Practiced comparison operators.

✅ Built a password checking program.

---

# Author

Mohamed Mohamed

Cybersecurity Academy