class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
employee_1 = Employee("Mehedi", 30, 280000) 
employee_2 = Employee("Lipu", 28, 300000)

print(f"Employee 1: {employee_1.name}, Age: {employee_1.age}, Salary: {employee_1.salary}")
print(f"Employee 2: {employee_2.name}, Age: {employee_2.age}, Salary: {employee_2.salary}")