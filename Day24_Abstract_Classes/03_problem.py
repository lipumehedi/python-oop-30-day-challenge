from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def work(self):
        pass


class Developer(Employee):

    def work(self):
        return f"{self.name} is writing Python code."


developer = Developer("Mehedi", 350000)

print(f"Name: {developer.name}")
print(f"Salary: ¥{developer.salary}")
print(developer.work())