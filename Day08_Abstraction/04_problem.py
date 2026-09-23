from abc import ABC, abstractmethod

class Employee(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass
    

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
      
    def calculate_salary(self):
       return self.monthly_salary
    

class PartTimeEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        
    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
      
        
    
employee1 = FullTimeEmployee("Mehedi", 300000)
employee2 = PartTimeEmployee("Rahim", 1500, 100)

print(employee1.name)
print(employee1.calculate_salary())

print(employee2.name)
print(employee2.calculate_salary())

employees = [employee1, employee2]

for employee in employees:
    print(f"{employee.name}'s salary: {employee.calculate_salary()} yen")