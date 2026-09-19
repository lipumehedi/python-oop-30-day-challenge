class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def get_annual_salary(self):
        return self.salary*12

employee1 = Employee("Mehedi", 280000)

annual_salary = employee1.get_annual_salary()

print(annual_salary)