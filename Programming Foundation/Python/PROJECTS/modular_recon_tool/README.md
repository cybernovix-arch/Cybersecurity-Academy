# 🛡️ Modular Recon Tool

## Overview

The **Modular Recon Tool** is an educational Python-based network reconnaissance simulator.

The purpose of this project is to demonstrate how cybersecurity tools can be designed using **modular programming principles**.

Instead of placing all functionality into one large Python file, the project separates different responsibilities into individual modules:

- Scanner module
- Reporting module
- Utility module
- Main controller

This project simulates port scanning for learning purposes and does not perform real network scanning.

---

# Features

- ✅ Simulated port scanning
- ✅ Modular Python architecture
- ✅ Security scan report generation
- ✅ Banner display system
- ✅ Dictionary-based result processing
- ✅ Separation of responsibilities between modules
- ✅ Function-based programming design

---

# Project Structure

```text
modular_recon_tool/

│
├── main.py
│       Main program controller
│
├── scanner.py
│       Handles simulated port scanning logic
│
├── reporter.py
│       Generates security scan reports
│
├── utils.py
│       Contains reusable utility functions
│
└── README.md
        Project documentation
```

---

# How It Works

The program follows this workflow:

```text
                    START

                      |
                      ▼

                   main.py

                      |
                      ▼

              Display Program Banner

                      |
                      ▼

              Define Target System

                      |
                      ▼

              Run Scanner Module

                      |
                      ▼

                scanner.py

                      |
                      ▼

             Return Scan Results

                      |
                      ▼

              reporter.py

                      |
                      ▼

              Generate Report

                      |
                      ▼

                    END
```

---

# Architecture

```text
                  Modular Recon Tool

                         |
                         ▼

                      main.py

          ┌──────────────┼──────────────┐

          ▼              ▼              ▼

    scanner.py     reporter.py      utils.py

    Scan Logic      Reports        Helper Tools
```

Each module has one responsibility:

### scanner.py

Responsible for:

- Receiving ports
- Checking simulated port status
- Returning scan results

---

### reporter.py

Responsible for:

- Receiving scan data
- Formatting results
- Displaying the security report

---

### utils.py

Responsible for:

- Reusable helper functions
- Displaying the project banner

---

### main.py

Responsible for:

- Controlling program execution
- Connecting all modules together

---

# Technologies Used

- Python 3
- Functions
- Lists
- Dictionaries
- Loops
- Conditional statements
- Parameters
- Return values
- Python modules
- Import statements

---

# How To Run

Navigate into the project directory:

```bash
cd modular_recon_tool
```

Run the program:

```bash
python main.py
```

---

# Example Output

```text
==============================
   CYBERSECURITY ACADEMY
   MODULAR RECON TOOL v1.0
==============================

===== SECURITY SCAN REPORT =====
Target: 192.168.1.10
--------------------------------
Port 21: CLOSED
Port 22: OPEN
Port 80: OPEN
Port 443: OPEN
Port 3306: CLOSED
--------------------------------
```

---

# Learning Outcomes

Through this project, I practiced:

- Creating and using Python functions
- Understanding function parameters
- Using return values
- Working with lists and dictionaries
- Using loops and conditional logic
- Creating Python modules
- Importing functions between files
- Designing modular software architecture
- Applying separation of concerns

---

# Cybersecurity Concepts Demonstrated

This project introduces foundational concepts used in cybersecurity tooling:

- Reconnaissance workflow
- Data collection and processing
- Report generation
- Automation using Python
- Tool organization and architecture

---

# Disclaimer

This project is created for educational purposes only.

The scanner functionality is simulated and does not perform real network scanning or interact with external systems.

Always perform security testing only on systems you own or have explicit permission to test.

---

# Project Status

✅ Completed — Version 1.0

Future improvements may include:

- User input for targets
- Command-line arguments
- File-based reports
- Logging functionality
- Real networking concepts in later cybersecurity modules
