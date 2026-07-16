# Lesson 3 - Loops

## Objective

The objective of this lesson is to learn how to use loops to execute repetitive tasks efficiently. Loops reduce code duplication and are widely used in automation, data processing, and cybersecurity.

## What is a Loop?

A loop is a programming structure that repeatedly executes a block of code until a specified condition is met or until all items in a sequence have been processed.

## Types of Loops Learned

### For Loop

A `for` loop is used to iterate through sequences such as lists, strings, and ranges.

Example:

```python
for number in range(1, 6):
    print(number)
```

### While Loop

A `while` loop repeatedly executes code as long as a condition remains true.

Example:

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

## Loop Control Statements Learned

### break

Stops a loop immediately.

### continue

Skips the current iteration and continues with the next one.

### else

Executes after a loop finishes normally without encountering a `break` statement.

## Nested Loops

A nested loop is a loop inside another loop. The inner loop completes all of its iterations for every iteration of the outer loop.

Example:

```python
for row in range(1, 4):
    for column in range(1, 4):
        print(column, end=" ")
    print()
```

Output:

```
1 2 3
1 2 3
1 2 3
```

## My Code

```python
for row in range(1, 6):
    for column in range(1, row + 1):
        print(column, end=" ")
    print()
```

Output:

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

## Mini Project

A simple **Port Scanner Simulator** was created to demonstrate how loops can automate repetitive tasks.

Example:

```python
ports = [21, 22, 25, 53, 80, 110, 143, 443]

open_ports = [22, 80, 443]

for port in ports:
    if port in open_ports:
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED")
```

## Cybersecurity Example

Loops are commonly used to:

- Scan multiple ports
- Scan IP address ranges
- Perform password brute-force attacks
- Automate reconnaissance
- Parse log files
- Fuzz applications
- Enumerate directories and files

Example:

```python
for port in range(20, 26):
    print(f"Scanning port {port}...")
```

## What I Learned

In this lesson I learned:

- What loops are.
- The difference between `for` and `while` loops.
- How to use the `range()` function.
- How to use `break`, `continue`, and `else`.
- How nested loops work.
- How loops are applied in cybersecurity automation.

## Files

- `L3_loops.py`
- `port_scanner_simulator.py`
- `README.md`

## Author

**Mohamed Mohamed**

**Cybersecurity Academy**
