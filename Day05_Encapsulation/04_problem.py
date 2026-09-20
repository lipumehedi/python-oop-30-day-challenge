class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def show_salary(self):
        return self.salary    

employee1 = Employee("Mehedi", 300000)

print(employee1.show_salary())