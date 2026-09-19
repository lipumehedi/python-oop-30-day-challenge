class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
employee_1 = Employee("Mehedi", 30, 280000) 
employee_2 = Employee("Lipu", 28, 300000)

print(
    f"Employee 1: {employee_1.name}\n"
    f"Age: {employee_1.age}\n"
    f"Salary: {employee_1.salary}\n"
)

print(
    f"Employee 2: {employee_2.name}\n"
    f"Age: {employee_2.age}\n"
    f"Salary: {employee_2.salary}"
)