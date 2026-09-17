class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        
employee = Employee("Mehedi", 30, 280000)

print(
    f"  Name: {employee.name}\n"
    f"   Age: {employee.age}\n"
    f"Salary: {employee.salary}"
)

employee.salary = 320000

print(
    f"  Name: {employee.name}\n"
    f"   Age: {employee.age}\n"
    f"Salary: {employee.salary}"
)