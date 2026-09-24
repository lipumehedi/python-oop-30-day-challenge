# Day 09 – Composition

## Topics Covered

- Composition
- Has-a relationship
- Objects inside other objects
- Reusing classes
- Building complex objects from smaller objects

## Practice

### Problem 1
Create an `Engine` class and use it inside a `Car` class.

### Problem 2
Create a `Battery` class and use it inside an `ElectricCar` class.

### Problem 3
Create a `Student` class and a `Course` class using composition.

### Problem 4
Create a real-world composition example using multiple classes.

## Goal

Understand how composition allows one class to contain and use objects of another class.

## Key Concept

Composition represents a **has-a** relationship.

Example:

```python
class Car:
    def __init__(self):
        self.engine = Engine()