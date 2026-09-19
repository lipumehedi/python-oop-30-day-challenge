class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def is_high_salary(self):
        return self.salary >= 300000 

employee1 = Employee("Mehedi", 280000)
employee2 = Employee("Karim", 350000)

print(employee1.is_high_salary())
print(employee2.is_high_salary())