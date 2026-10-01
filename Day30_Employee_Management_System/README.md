# Day 30 – Employee Management System

## Overview

This is the final project of the **Python OOP 30-Day Challenge**.

The Employee Management System is a practical Python application that combines Object-Oriented Programming, file handling, JSON data storage, validation, exception handling, and unit testing.

The system allows users to create, manage, search, update, delete, save, and load employee records.

---

## Features

* Create employee records
* Display employee information
* Add employees
* Show all employees
* Search employees by ID
* Update employee salary
* Delete employees
* Validate employee information
* Handle invalid data with exceptions
* Save employee data to JSON
* Load employee data from JSON
* Unit testing with `unittest`

---

## Project Structure

```text
Day30_Employee_Management_System/
│
├── employee.py
├── manager.py
├── main.py
├── test_employee.py
├── employees.json
└── README.md
```

### File Description

| File               | Description                                |
| ------------------ | ------------------------------------------ |
| `employee.py`      | Employee class, attributes, and validation |
| `manager.py`       | Employee management operations             |
| `main.py`          | Main application and program execution     |
| `test_employee.py` | Unit tests using `unittest`                |
| `employees.json`   | Employee data storage                      |
| `README.md`        | Project documentation                      |

---

## Main Operations

The system supports:

1. Add Employee
2. Show All Employees
3. Search Employee
4. Update Salary
5. Delete Employee
6. Save Employee Data
7. Load Employee Data
8. Validate Employee Data
9. Handle Exceptions
10. Run Unit Tests

---

## Example Employee

```text
Name: Mehedi Lipu
Employee ID: E001
Position: Python Developer
Salary: ¥500000
```

---

## JSON Data Storage

Employee information is stored in `employees.json`.

Example:

```json
[
    {
        "name": "Mehedi Lipu",
        "employee_id": "E001",
        "position": "Python Developer",
        "salary": 500000
    }
]
```

The program automatically creates and updates the JSON file when `save_to_file()` is called.

Employee data can later be loaded using `load_from_file()`.

---

## Validation and Exception Handling

The project validates employee information before creating employee objects.

Examples of invalid data:

* Empty employee name
* Empty employee ID
* Empty position
* Salary less than or equal to zero
* Invalid salary updates

Example:

```python
try:
    employee = Employee(
        "Mehedi Lipu",
        "E001",
        "Python Developer",
        -50000
    )

except ValueError as e:
    print(f"Error: {e}")
```

Output:

```text
Error: Salary must be greater than 0.
```

---

## Unit Testing

The project uses Python's built-in `unittest` framework.

Tests cover:

* Employee creation
* Employee information
* Salary updates
* Employee validation
* Invalid salary
* Empty employee name
* Adding employees
* Deleting employees
* Manager salary updates
* Exception handling

Run the tests with:

```bash
python test_employee.py
```

Expected result:

```text
........
----------------------------------------------------------------------
Ran 8 tests

OK
```

---

## How to Run

### Step 1: Clone the repository

```bash
git clone <your-repository-url>
```

### Step 2: Open the project

```bash
cd Day30_Employee_Management_System
```

### Step 3: Run the application

```bash
python main.py
```

### Step 4: Run unit tests

```bash
python test_employee.py
```

---

## Technologies

* Python 3
* Object-Oriented Programming
* JSON
* File Handling
* Exception Handling
* Unit Testing
* `unittest`

---

## OOP Concepts Used

This final project combines concepts learned throughout the 30-Day Challenge:

* Classes and Objects
* Constructors
* Instance Attributes
* Instance Methods
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* SOLID Principles
* Exception Handling
* File Handling
* Object Relationships
* Unit Testing
* Design Patterns

---

## Learning Outcomes

After completing this project, I practiced how to:

* Design classes for a real-world application
* Manage multiple objects
* Separate application responsibilities across files
* Store data using JSON
* Load persistent data from files
* Validate user and employee information
* Handle exceptions safely
* Write unit tests
* Organize a Python project professionally
* Combine multiple OOP concepts into one application

---

## Project Status

**Completed ✅**

This project is the final project of my **Python OOP 30-Day Challenge**.

---

## Author

**Mehedi Lipu**

Python Backend Developer — Learning & Building in Japan

### GitHub

`https://github.com/lipumehedi`

---

## Python OOP 30-Day Challenge

This project is part of my complete Python OOP learning journey:

**Day 01 → Day 30**

From basic Classes & Objects to a complete Employee Management System.

🚀 **Keep Learning. Keep Building.**
