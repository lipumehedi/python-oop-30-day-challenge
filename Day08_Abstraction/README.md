# Day 08 – Abstraction

## Topics Covered

* Abstraction
* Abstract classes
* Abstract methods
* `abc` module
* `ABC`
* `@abstractmethod`
* Implementing abstract methods
* Common structure for child classes

## Practice

### Problem 1

Create an abstract `Animal` class with an abstract `speak()` method.

### Problem 2

Create different child classes and implement the abstract method.

### Problem 3

Create an abstract `Payment` class and implement different payment methods.

### Problem 4

Create a real-world abstraction example using an abstract class.

## Goal

Understand how abstraction defines what a class must do without specifying exactly how it should do it.

## Key Concept

An abstract class provides a common structure for child classes.

Child classes must implement the required abstract methods.

Example:

```python
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def speak(self):
        pass
```
