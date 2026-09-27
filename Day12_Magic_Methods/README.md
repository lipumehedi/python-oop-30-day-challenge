# Day 12 – Magic Methods (Dunder Methods)

## Topics Covered

- Magic methods (dunder methods)
- __str__()
- __repr__()
- __len__()
- __eq__()
- Customizing object behavior

## Practice

### Problem 1 – Student Representation
Create a Student class and use __str__() to display student information.

### Problem 2 – Book Length
Create a Book class and use __len__() to return the number of pages.

### Problem 3 – Product Comparison
Create a Product class and use __eq__() to compare two products by price.

### Problem 4 – Employee Representation
Create an Employee class and use __repr__() to display employee information.

## Goal

Understand how magic methods customize the behavior of Python objects.

## Key Concept

Magic methods are special methods with double underscores before and after their names.

Example:

    class Student:
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return self.name

    student = Student("Mehedi")
    print(student)

Output:

    Mehedi
    