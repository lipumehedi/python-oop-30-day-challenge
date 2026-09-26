# Day 11 – Static Methods

## Topics Covered

- Static methods
- `@staticmethod` decorator
- Static methods vs instance methods
- Static methods vs class methods
- Utility methods
- Calling static methods using a class or object

## Practice

### Problem 1 – Calculator
Create a `Calculator` class with a static method to add two numbers.

### Problem 2 – Temperature Converter
Create a `TemperatureConverter` class with static methods to convert Celsius to Fahrenheit and Fahrenheit to Celsius.

### Problem 3 – Number Utility
Create a `NumberUtility` class with static methods to check whether a number is even and whether it is positive.

### Problem 4 – Employee Utility
Create an `Employee` class with a static method to validate whether a salary amount is valid.

## Goal

Understand how static methods work and when to use them for operations that do not require instance or class-level data.

## Key Concept

A static method uses the `@staticmethod` decorator and does not require `self` or `cls`.

Example:

```python
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
```
