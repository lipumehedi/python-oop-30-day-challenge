# Day 10 – Class Variables & Class Methods

## Topics Covered

* Class variables
* Instance variables
* Difference between class variables and instance variables
* `@classmethod`
* `cls`
* Accessing class variables
* Modifying class-level data
* Shared data between objects

## Practice

### Problem 1 – Class Variable

Create an `Employee` class with a class variable `company`.

Create multiple employee objects and access the shared company name.

### Problem 2 – Class Method

Create a `Student` class with a class variable `school`.

Create a class method to change the school name.

### Problem 3 – Employee Counter

Create an `Employee` class that counts how many employee objects have been created.

Use a class variable and update it whenever a new employee object is created.

### Problem 4 – Bank

Create a `Bank` class with a class variable `bank_name`.

Use a class method to change the bank name.

Create multiple bank account objects and observe how the shared bank name changes.

## Goal

Understand the difference between instance-level data and class-level data.

Learn how class variables are shared between objects and how `@classmethod` can be used to access and modify class-level information.

## Key Concepts

### Class Variable

A class variable belongs to the class and is shared by all objects.

Example:

```python
class Employee:
    company = "ABC Company"
```

### Instance Variable

An instance variable belongs to a specific object.

Example:

```python
class Employee:
    def __init__(self, name):
        self.name = name
```

### Class Method

A class method works with the class instead of a specific object.

It uses the `@classmethod` decorator and `cls` parameter.

Example:

```python
class Employee:
    company = "ABC Company"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
```

## Difference

| Type              | Belongs To | Access                 |
| ----------------- | ---------- | ---------------------- |
| Class Variable    | Class      | `ClassName.variable`   |
| Instance Variable | Object     | `object.variable`      |
| Class Method      | Class      | `@classmethod` + `cls` |

## Expected Outcome

By the end of Day 10, you should understand:

* How class variables work
* How instance variables differ from class variables
* How `@classmethod` works
* How `cls` refers to the class
* How multiple objects can share class-level data
* How to modify class-level data using a class method
