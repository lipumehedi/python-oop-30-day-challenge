#Employee Method
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def show_info(self):
        print(f"Name: {self.name} \nSalary: {self.salary}")
        

employee1 = Employee("Mehedi", 280000)
employee1.show_info()