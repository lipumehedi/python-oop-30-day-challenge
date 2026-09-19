class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def calculate_total_salary(self, months):
        return self.salary * months

employee1 = Employee("Mehedi", 280000)
total = employee1.calculate_total_salary(6)
print(total)   