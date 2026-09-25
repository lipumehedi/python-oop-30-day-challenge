class Employee:
    employee_count = 0
    
    
    def __init__(self, name):
        self.name = name
        Employee.employee_count += 1
    
    @classmethod
    def show_count(cls):  
        return cls.employee_count

employee1 = Employee("Mehedi")
employee2 = Employee("Rahim")
employee3 = Employee("Karim")

print(Employee.show_count())